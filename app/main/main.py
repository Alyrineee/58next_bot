from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.main.main_keyboards import main_keyboard

main = Router()

@main.message(Command("second_start"))
async def start(message: Message):

    # Пока бд нету, используем два старта xD
    return await message.answer(
        "Добро пожаловать, выбери пункт в меню",
        reply_markup=main_keyboard
    )


@main.callback_query(F.data == "teams")
async def teams_callback(callback: CallbackQuery):
    await callback.answer()
    return await callback.message.answer("Команды")


@main.callback_query(F.data == "events")
async def events_callback(callback: CallbackQuery):
    await callback.answer()
    return await callback.message.answer("События")


@main.callback_query(F.data == "rating")
async def rating_callback(callback: CallbackQuery):
    await callback.answer()
    return await callback.message.answer("Рейтинг")


@main.callback_query(F.data == "profile")
async def profile_callback(callback: CallbackQuery):
    await callback.answer()
    return await callback.message.answer("Профиль")