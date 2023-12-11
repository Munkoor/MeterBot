import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from handlers import commands, queries
from handlers.commanders import set_commands

dp = Dispatcher()

load_dotenv()


async def start_bot(bot: Bot):
    await set_commands(bot)


async def main() -> None:
    dp.startup.register(start_bot)
    dp.include_routers(commands.router, queries.router)

    await dp.start_polling(Bot(token=os.getenv("BOT_TOKEN"), parse_mode="HTML"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
