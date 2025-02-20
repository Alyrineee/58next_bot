import asyncio

from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.utils.paginate_keyboard import paginate_inline_keyboard

auth = Router()

@auth.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветик, не могу найти тебя в базе( Надо пройти регистрацию")
    await asyncio.sleep(2)

    # Это пока тестовый вариант: ) Не судите строго
    await message.answer(
        "Чтобы зарегистрироваться выбери класс",
        reply_markup=paginate_inline_keyboard(
            [["9b", "9Б"]],
            1,
            "auth",
        ),
    )


