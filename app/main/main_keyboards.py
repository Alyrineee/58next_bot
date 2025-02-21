from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

main_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Команды",
                    callback_data="teams",
                ),
                InlineKeyboardButton(
                    text="События",
                    callback_data="events",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Рейтинг",
                    callback_data="rating",
                ),
                InlineKeyboardButton(
                    text="Профиль",
                    callback_data="profile",
                ),
            ],
        ],
    )
