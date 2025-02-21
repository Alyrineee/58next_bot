from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

auth_confirm_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Окей",
                    callback_data="rules_confirm",
                ),
            ],
        ],
    )
