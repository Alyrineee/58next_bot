import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from app.auth.auth_keyboards import auth_confirm_keyboard
from app.database.requests import request_user_object
from app.utils.paginate_keyboard import paginate_inline_keyboard

auth = Router()

@auth.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветик, не могу найти тебя в базе( Надо пройти регистрацию")
    await asyncio.sleep(2)

    # Это пока тестовый вариант: ) Не судите строго
    return await message.answer(
        "Чтобы зарегистрироваться выбери класс",
        reply_markup=paginate_inline_keyboard(
            [["9Б", "9Б"]],
            1,
            "auth",
        ),
    )

@auth.callback_query(F.data.startswith("auth"))
async def auth_callback(callback: CallbackQuery):
    await callback.answer()
    await request_user_object(
        telegram_id=callback.message.chat.id,
        user_class=callback.data.split("#")[1],
    )
    return await callback.message.answer(
        "Отлично, теперь ты зарегистрирован! Вкратце расскажу зачем этот бот <введите текст>",
        reply_markup=auth_confirm_keyboard
    )

