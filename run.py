import asyncio
import logging
import os
from dotenv import main

from aiogram import Bot, Dispatcher

from app.auth import auth

main.load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_routers(auth)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit...")
