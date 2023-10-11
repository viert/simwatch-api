import asyncio

import aiohttp

from typing import List, Dict, Any, Optional
from asyncio.queues import Queue
import grpc.aio
from croydon import ctx
from app.proto.stub import get_new_stub
from app.proto.camden_pb2 import (
    QueryRequest,
    QuerySubscription,
    QuerySubscriptionRequest,
    QuerySubscriptionUpdate,
    SUBSCRIPTION_ADD,
    SUBSCRIPTION_DELETE,
    ONLINE,
    OFFLINE,
    FLIGHTPLAN
)
from app.models import Chat, Subscription

from .api_types import Message

BASE_URI = "https://api.telegram.org/bot"


class TelegramBot:

    token: str
    poll_timeout: int
    queue: Queue

    def __init__(self, *, token: str, poll_timeout: int):
        self.token = token
        self.poll_timeout = poll_timeout
        self.queue = Queue()

    async def check(self) -> bool:
        response = await self.api_request_raw("GET", "/getMe")
        data = await response.json()
        ctx.log.debug(f"/getMe response {data}")
        return response.status == 200

    async def api_request_raw(self,
                              method: str,
                              path: str,
                              data: Optional[Dict[str, Any]] = None) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            url = f"{BASE_URI}{self.token}{path}"
            async with session.request(method, url, json=data) as response:
                return response

    async def api_request(self,
                          method: str,
                          path: str,
                          data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        response = await self.api_request_raw(method, path, data)
        return await response.json()

    async def send_text(self, chat_id: int, text: str, *, disable_md: bool = False):
        data = {
            "chat_id": chat_id,
            "text": text,
        }
        if not disable_md:
            data["parse_mode"] = "Markdown"

        resp = await self.api_request_raw("POST", "/sendMessage", data)
        if resp.status >= 400:
            ctx.log.error("error")

    async def process_command(self, message: Message, chat: Chat):
        cmd = message.command()
        if cmd is None:
            return

        cmd_text = cmd.text[1:]
        cmd_method = f"cmd_{cmd_text}"
        if hasattr(self, cmd_method):
            ctx.log.debug(f"processing \"{cmd_text}\" command from chat {chat.chat_id} with @{chat.username}")
            await getattr(self, cmd_method)(message, chat)
        else:
            ctx.log.debug(f"unrecognised command \"{cmd_text}\" from chat {chat.chat_id} with @{chat.username}")

    @staticmethod
    async def setup_chat(message: Message) -> Optional[Chat]:
        chat_data = message.chat
        if chat_data and chat_data.type == "private":
            chat = await Chat.get(f"{chat_data.id}")
            if chat is None:
                chat = Chat.create(
                    chat_id=f"{chat_data.id}",
                    first_name=chat_data.first_name,
                    last_name=chat_data.last_name,
                    username=chat_data.username,
                )
                await chat.save()
            return chat
        return None

    async def cmd_start(self, _: Message, chat: Chat):
        await self.send_text(chat.chat_id, "Hello, this is *SimWatch*, how can I help?")

    async def cmd_ping(self, _: Message, chat: Chat):
        await self.send_text(chat.chat_id, "pong")

    async def cmd_list(self, _: Message, chat: Chat):
        subs = await chat.subscriptions().all()
        if not subs:
            await self.send_text(chat.chat_id, "You have no active subscriptions, "
                                               "you can subscribe with `/subscribe {query}` command")
        else:
            text = f"You are subscribed to {len(subs)} "
            text += "query" if len(subs) == 1 else "queries"
            text += "\n\n"
            for sub in subs:
                text += f"id: `{sub.id}`\n"
                text += f"query: `{sub.query}`\n\n"
            await self.send_text(chat.chat_id, text)

    async def cmd_subscribe(self, message: Message, chat: Chat):
        cmd = message.command()
        args = message.text[cmd.offset+cmd.length:].strip()
        if not args:
            await self.send_text(chat.chat_id, "Query is missing, use `/subscribe {query}` to "
                                               "subscribe for certain pilots")
            return

        stub = get_new_stub()
        try:
            response = await stub.CheckQuery(QueryRequest(query=args))
        except grpc.aio.AioRpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                await self.send_text(chat.chat_id, "GRPC service is unavailable, sorry about that, we might be "
                                                   "taking care of it already")
            else:
                await self.send_text(chat.chat_id, e.details(), disable_md=True)
            return

        if not response.valid:
            await self.send_text(chat.chat_id, f"Query is invalid: {response.error_message}", disable_md=True)
            return

        sub = Subscription.create(chat_id=chat.id, query=args)
        await sub.save()

        await self.queue.put({"type": "subscribe", "sub_id": f"{sub.id}", "query": sub.query})

        await self.send_text(chat.chat_id, f"You have subscribed to query `{args}`")

    async def cmd_unsubscribe(self, message: Message, chat: Chat):
        cmd = message.command()
        args = message.text[cmd.offset+cmd.length:].strip()

        if not args:
            await self.send_text(chat.chat_id, "Subscription ID is missing, use `/unsubscribe {id}` to "
                                               "unsubscribe\\. Use /list command to list your active subscriptions")
            return

        sub = await Subscription.get(args)
        if not sub or sub.chat_id != chat.id:
            await self.send_text(chat.chat_id, f"Cannot find subscription `{args}`\\. "
                                               f"Use /list command to list your active subscriptions")
            return

        await self.queue.put({"type": "unsubscribe", "sub_id": f"{sub.id}"})

        await sub.destroy()
        await self.send_text(chat.chat_id, f"You have successfully unsubscribed from query `{sub.query}`")

    async def process_updates(self, updates: List[Dict[str, Any]]) -> int:
        update_id = 0
        for update in updates:
            new_update_id = update.get("update_id")
            if new_update_id and new_update_id > update_id:
                update_id = new_update_id

            message = update.get("message")
            if not message:
                continue
            message = Message(**message)
            chat = await self.setup_chat(message)
            if chat:
                await self.process_command(message, chat)
        return update_id + 1

    async def _poll_updates(self):
        update_id = 0
        timeout = aiohttp.ClientTimeout(total=self.poll_timeout)
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    url = f"{BASE_URI}{self.token}/getUpdates?offset={update_id}&timeout={self.poll_timeout}"
                    async with session.get(url, timeout=timeout) as response:
                        data = await response.json()
                        if data["result"]:
                            update_id = await self.process_updates(data["result"])
                except asyncio.TimeoutError:
                    continue

    async def _read_queue(self) -> Dict[str, str]:
        ctx.log.debug("waiting for an item from queue")
        item = await self.queue.get()
        return item

    async def notify(self, update: QuerySubscriptionUpdate):
        ctx.log.debug("calculating notification")
        sub_id = update.subscription_id
        sub = await Subscription.get(sub_id)
        if sub is None:
            ctx.log.error(f"can't notify user on sub_id {sub_id}: subscription not found")
        chat = await sub.chat()
        if chat is None:
            ctx.log.error(f"can't notify user on sub_id {sub_id}: subscription is broken, no chat found")
        pilot = update.pilot

        text = f"Pilot *{pilot.name}* _cid={pilot.cid}_ as *{pilot.callsign}*"

        if update.update_type == ONLINE:
            text += " is *Online*"
        elif update.update_type == OFFLINE:
            text += " went *Offline*"
        elif update.update_type == FLIGHTPLAN:
            text += " has filed a flight plan"

        if pilot.aircraft_type is not None:
            text += f"\nThey're flying {pilot.aircraft_type.manufacturer_code} {pilot.aircraft_type.name}"

        if pilot.flight_plan is not None:
            fp = pilot.flight_plan
            text += f"\n*{fp.departure} - {fp.arrival}* at {fp.deptime}\n" \
                    f"Cruising altitude *{fp.altitude}*\n" \
                    f"Remarks: _{fp.remarks}_"

        text += f"\n\n_Matching your subscription to_ `{sub.query}` `{sub.id}`"

        await self.send_text(chat.chat_id, text)

    async def _run_grpc(self):
        stub = get_new_stub()
        conn = stub.SubscribeQuery()

        tasks = {
            asyncio.create_task(conn.read(), name="grpc"),
            asyncio.create_task(self._read_queue(), name="queue")
        }

        subs = await Subscription.all()
        for sub in subs:
            req = QuerySubscriptionRequest(
                request_type=SUBSCRIPTION_ADD,
                subscription=QuerySubscription(
                    id=f"{sub.id}",
                    query=sub.query,
                )
            )
            await conn.write(req)

        while True:
            done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            while done:
                task = done.pop()
                match task.get_name():
                    case "grpc":
                        exc = task.exception()
                        if exc is not None:
                            if isinstance(exc, grpc.aio.AioRpcError):
                                if exc.code() == grpc.StatusCode.UNAVAILABLE:
                                    ctx.log.error("GRPC unavailable while reading subs")
                            else:
                                ctx.log.error(f"exception while reading subs from GRPC: {exc}")
                            continue
                        update = task.result()
                        ctx.log.info(f"got a GRPC update")
                        tasks.add(asyncio.create_task(self.notify(update), name="notify"))
                        tasks.add(asyncio.create_task(conn.read(), name="grpc"))
                    case "queue":
                        exc = task.exception()
                        if exc is not None:
                            ctx.log.error(f"exception while reading subs from GRPC: {exc}")
                            continue
                        item = task.result()
                        ctx.log.info(f"got a new subscription item from queue")
                        if item["type"] == "subscribe":
                            req = QuerySubscriptionRequest(
                                request_type=SUBSCRIPTION_ADD,
                                subscription=QuerySubscription(
                                    id=item["sub_id"],
                                    query=item["query"],
                                )
                            )
                        elif item["type"] == "unsubscribe":
                            req = QuerySubscriptionRequest(
                                request_type=SUBSCRIPTION_DELETE,
                                subscription=QuerySubscription(
                                    id=item["sub_id"],
                                    query="",
                                )
                            )
                        else:
                            raise RuntimeError("this branch must be unreachable")

                        ctx.log.debug(f"forwarding request to grpc \n{req}")
                        tasks.add(asyncio.create_task(conn.write(req), name="forward_to_grpc"))
                        tasks.add(asyncio.create_task(self._read_queue(), name="queue"))
                    case _:
                        exc = task.exception()
                        if exc is not None:
                            ctx.log.error(f"error executing task {task.get_name()}: {exc}")
                        else:
                            ctx.log.debug(f"task {task.get_name()} completed")

    async def run(self):
        if not await self.check():
            ctx.log.error("can't start bot, getMe returned non-successful status code")
            return

        tasks = {
            asyncio.create_task(self._poll_updates()),
            asyncio.create_task(self._run_grpc())
        }

        await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

