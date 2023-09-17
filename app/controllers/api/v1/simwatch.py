import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import PlainTextResponse
from google.protobuf.json_format import MessageToDict
from croydon import ctx
from app.proto.stub import get_new_stub
from app.proto.camden_pb2 import QueryRequest, NoParams
from app.types import (
    MapBoundsRequest,
    MapFilterRequest,
    MapWeatherRequest,
    QueryResponse,
    GRPCBuildInfo,
)


simwatch_ctrl = APIRouter(prefix="/api/v1/simwatch")


@simwatch_ctrl.websocket("/")
async def map_updates(websocket: WebSocket):
    await websocket.accept()
    stub = get_new_stub()
    grpc_updates = stub.MapUpdates()

    tasks = {
        asyncio.create_task(grpc_updates.read(), name="grpc"),
        asyncio.create_task(websocket.receive_json(), name="ws")
    }

    try:
        while True:
            done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            done = done.pop()
            match done.get_name():
                case "grpc":
                    update = done.result()
                    update = MessageToDict(update)
                    tasks.add(asyncio.create_task(websocket.send_json(update)))
                    tasks.add(asyncio.create_task(grpc_updates.read(), name="grpc"))
                case "ws":
                    req = done.result()
                    req_type = req.get("request_type")
                    match req_type:
                        case "map_bounds":
                            req = MapBoundsRequest(**req)
                        case "filter":
                            req = MapFilterRequest(**req)
                        case "wx":
                            req = MapWeatherRequest(**req)
                        case _:
                            await websocket.send_json({"error": f"request type {req_type} is not supported"})
                            continue

                    grpc_req = req.to_grpc()
                    tasks.add(asyncio.create_task(websocket.send_json({"status": "request forwarded"})))
                    tasks.add(asyncio.create_task(grpc_updates.write(grpc_req)))
                    tasks.add(asyncio.create_task(websocket.receive_json(), name="ws"))
                case _:
                    ctx.log.debug(f"task finished {done}")
    except WebSocketDisconnect:
        return


@simwatch_ctrl.get("/checkquery/{query}")
async def check_query(query: str) -> QueryResponse:
    stub = get_new_stub()
    resp = await stub.CheckQuery(QueryRequest(query=query))
    return QueryResponse(valid=resp.valid, error=resp.error_message or None)


@simwatch_ctrl.get("/build_info")
async def grpc_build_info() -> GRPCBuildInfo:
    stub = get_new_stub()
    info = await stub.BuildInfo(NoParams())
    return GRPCBuildInfo(
        name=info.name,
        version=info.version,
        repository=info.repository,
        license=info.license,
    )


@simwatch_ctrl.get("/metrics", response_class=PlainTextResponse)
async def grpc_metrics() -> str:
    stub = get_new_stub()
    metrics = await stub.GetMetricsText(NoParams())
    return metrics.text
