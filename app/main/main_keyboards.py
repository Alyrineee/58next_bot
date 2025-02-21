from multiprocessing.reduction import register

from aiogram.filters import callback_data
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

register_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Записаться",
                callback_data="register",
            ),
        ],
    ],
)

