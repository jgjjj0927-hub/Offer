from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

OFFER_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❌ Отозвать", callback_data="revoke_offer"),
            InlineKeyboardButton(text="✅ Обменять", callback_data="accept_offer"),
        ]
    ]
)
