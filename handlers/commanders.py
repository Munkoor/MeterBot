from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Getting started"
        ),
        BotCommand(
            command="meter",
            description="Provide address information, personal account, and photos of the meters"
        ),
        BotCommand(
            command="cancel",
            description="Cancel last action"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())