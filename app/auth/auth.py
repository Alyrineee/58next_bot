import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from app.auth.auth_keyboards import auth_confirm_keyboard
from app.database.requests import request_user_object, is_user_registered
from app.utils.paginate_keyboard import paginate_inline_keyboard

auth = Router()

@auth.message(CommandStart())
async def start(message: Message):
    if await is_user_registered(message.from_user.id):
        return await message.answer(
            "Приветик, нашел тебя в базе: )\n\nДобро пожаловать",
            reply_markup=auth_confirm_keyboard,
        )

    await message.answer("Приветик, не могу найти тебя в базе( Надо пройти регистрацию")
    await asyncio.sleep(2)
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

