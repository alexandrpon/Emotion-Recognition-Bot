import asyncio
from aiogram import Bot, Dispatcher
import logging
from Bot.set_config import config
from Bot.handlers import commands, images


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(commands.router, images.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


def launch_bot():
    asyncio.run(main())
