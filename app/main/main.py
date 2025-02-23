from aiogram import Router, F
from aiogram.loggers import event
from aiogram.types import CallbackQuery

from app.database.models import User
from app.database.requests import (request_user_object, get_events, get_event,
                                   add_user_to_event, is_user_added_event, remove_user_from_event)
from app.main.main_keyboards import main_keyboard, get_register_keyboard
from app.utils.paginate_keyboard import paginate_inline_keyboard

main = Router()
@main.callback_query(F.data == "rules_confirm")
async def start(callback: CallbackQuery):
    await callback.answer()
    return await callback.message.answer(
        "Добро пожаловать, выбери пункт в меню",
        reply_markup=main_keyboard
    )


@main.callback_query(F.data == "teams")
async def teams_callback(callback: CallbackQuery):
    await callback.answer()
    return await callback.message.answer("Пока не работает: (")


@main.callback_query(F.data == "events")
async def events_callback(callback: CallbackQuery):
    events = await get_events()
    await callback.answer()
    if events:
        return await callback.message.edit_text(
            "Выбери событие",
            reply_markup=paginate_inline_keyboard(
                events,
                1,
                "event"
            )
        )

    return await callback.message.answer("Пока событий нет: (")


@main.callback_query(F.data == "rating")
async def rating_callback(callback: CallbackQuery):
    await callback.answer()
    return await callback.message.answer("Пока не работает: (")


@main.callback_query(F.data == "profile")
async def profile_callback(callback: CallbackQuery):
    await callback.answer()
    user = await request_user_object(
        callback.message.chat.id
    )
    return await callback.message.answer(
        f"ID: {user.telegram_id}\n"
        f"Класс: {user.user_class}",
    )

@main.callback_query(F.data.startswith("event"))
async def event_detail_callback(callback: CallbackQuery):
    await callback.answer()
    event = await get_event(int(callback.data.split("#")[2]))
    await callback.message.edit_text(
        f"Название: {event.name}\n\n"
        f"Описание: {event.description}",
        reply_markup=get_register_keyboard(
            await is_user_added_event(
                user_id=callback.message.chat.id,
                event_id=1,
            ),
        ),
    )

@main.callback_query(F.data == "register")
async def register_callback(callback: CallbackQuery):
    await callback.answer()
    await add_user_to_event(
        user_id=callback.message.chat.id,
        event_id=1
    )
    await callback.message.answer(
        "Ты записался"
    )


@main.callback_query(F.data == "unregister")
async def register_callback(callback: CallbackQuery):
    await callback.answer()
    await remove_user_from_event(
        user_id=callback.message.chat.id,
        event_id=1
    )
    await callback.message.answer(
        "Ты отписался"
    )
