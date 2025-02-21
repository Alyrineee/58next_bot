import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.auth.auth import auth
from app.database.models import async_main
from app.main.main import main as main_router
from config import TOKEN


logging.basicConfig(level=logging.INFO)

async def main():
    dp = Dispatcher()
    dp.include_routers(auth, main_router)
    bot = Bot(token=TOKEN)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    await async_main()
    print('Starting up...')


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit...")
