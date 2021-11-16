from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from handlers.users.timetable import show_one_course, show_two_course, show_three_course, show_four_course
from keyboards.inline.Coursekeyboards import one_curse_number, level1, level1_keyboard, two_curse_number, \
    four_curse_number, three_curse_number
from keyboards.inline.callback_data import group_callback

from loader import dp


@dp.callback_query_handler(group_callback.filter(group=one_curse_number))
async def one(call: CallbackQuery, callback_data):
    await call.answer(cache_time=60)
    curse_number = callback_data.get("group")
    await call.message.answer(f"{show_one_course(curse_number)}", reply_markup=level1_keyboard)


@dp.callback_query_handler(group_callback.filter(group=two_curse_number))
async def one(call: CallbackQuery, callback_data):
    await call.answer(cache_time=60)
    curse_number = callback_data.get("group")
    await call.message.answer(f"{show_two_course(curse_number)}", reply_markup=level1_keyboard)

@dp.callback_query_handler(group_callback.filter(group=three_curse_number))
async def one(call: CallbackQuery, callback_data):
    await call.answer(cache_time=60)
    curse_number = callback_data.get("group")
    await call.message.answer(f"{show_three_course(curse_number)}", reply_markup=level1_keyboard)

@dp.callback_query_handler(group_callback.filter(group=four_curse_number))
async def one(call: CallbackQuery, callback_data):
    await call.answer(cache_time=60)
    curse_number = callback_data.get("group")
    await call.message.answer(f"{show_four_course(curse_number)}", reply_markup=level1_keyboard)

