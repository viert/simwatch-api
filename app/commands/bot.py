from croydon.command import Command
from croydon import ctx
from app.telegram.bot import TelegramBot


class Bot(Command):

    NAME = "bot"
    HELP = "run telegram bot"
    ASYNC_RUN = True

    async def run_async(self) -> None:
        token = ctx.cfg.bot.token
        poll_timeout = ctx.cfg.bot.poll_timeout
        bot = TelegramBot(token=token, poll_timeout=poll_timeout)
        await bot.run()
