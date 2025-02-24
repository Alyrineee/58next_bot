from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

auth_confirm_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Меню",
                    callback_data="rules_confirm",
                ),
            ],
        ],
    )
