from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import Menu_callback

Menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text=" I курс",
            callback_data=Menu_callback.new(course="первый")
        ),
        InlineKeyboardButton(
            text=" II курс",
            callback_data=Menu_callback.new(course="второй")
        )
    ],
    [
        InlineKeyboardButton(
            text="III курс",
            callback_data=Menu_callback.new(course="третий")
        ),
        InlineKeyboardButton(
            text="IV курс",
            callback_data=Menu_callback.new(course="четвертый")

        )
    ],
    [
        InlineKeyboardButton(
            text="Закрыть клавиатуру",
            callback_data=Menu_callback.new(course="cancel")
        )
    ]

])


