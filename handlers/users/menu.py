from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.Coursekeyboards import one_course, two_course, three_course, four_course
from keyboards.inline.Menukeyboards import Menu
from keyboards.inline.callback_data import Menu_callback, Menu_nextback
from loader import dp


@dp.message_handler(Command("Menu"))
async def menu(message: types.Message):
    await message.answer(text="Выберите ваш курc", reply_markup=Menu)


@dp.callback_query_handler(Menu_callback.filter(course="первый"))
async def menu1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Первый курс",
                              reply_markup=one_course)


@dp.callback_query_handler(Menu_callback.filter(course="второй"))
async def menu1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Второй курс",
                              reply_markup=two_course)


@dp.callback_query_handler(Menu_callback.filter(course="третий"))
async def menu1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Третий курс",
                              reply_markup=three_course)

@dp.callback_query_handler(Menu_callback.filter(course="четвертый"))
async def menu1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("четвертый курс",
                              reply_markup=four_course)

@dp.callback_query_handler(Menu_nextback.filter(nextback="level1"))
async def menu1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Выбрать курс",
                              reply_markup=Menu)

@dp.callback_query_handler(Menu_callback.filter(course="cancel"))
async def menu1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup()

