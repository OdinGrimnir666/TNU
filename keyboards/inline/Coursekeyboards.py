from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import openpyxl
from keyboards.inline.Menukeyboards import Menu
from keyboards.inline.callback_data import group_callback, Menu_nextback, Menu_callback

workbook = openpyxl.open("data.xlsx", read_only=True)
sheet = workbook.active



 

def vl(p):
    return str(sheet[p].value)


one_curse_number = [vl("M12"), vl("N12"), vl("O12"), vl("P12"), vl("Q12"), vl("R12"),
                    vl("S12"), vl("T12"), vl("U12")]
list_num=[]
for i in one_curse_number[0]:
    try:
        num=int(i)
        list_num.append(str(num))

    except ValueError:
        continue
print(list_num)


two_curse_number = [vl("X12"), vl("Y12"), vl("Z12"), vl("AA12"), vl("AB12"), vl("AC12")
    , vl("AD12"), vl("AE12"), vl("AF12"), vl("AG12")]

three_curse_number = [vl("AJ12"), vl("AK12"), vl("AL12"), vl("AM12"), vl("AN12"),
                      vl("AO12"), vl("AP12"), vl("AQ12"), vl("AR12"), vl("AS12")]

four_curse_number = [vl("AV12"), vl("AW12"), vl("AX12"), vl("AY12"), vl("AZ12"), vl("BA12"), vl("BB12"),
                     vl("BC12"), vl("BD12"), vl("BE12")]

one_course = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(
            text=one_curse_number[0],
            callback_data=group_callback.new(group=one_curse_number[0])
        ),
        InlineKeyboardButton(
            text=one_curse_number[1],
            callback_data=group_callback.new(group=one_curse_number[1])
        ),
        InlineKeyboardButton(
            text=one_curse_number[2],
            callback_data=group_callback.new(group=one_curse_number[2])
        )
    ],
    [
        InlineKeyboardButton(
            text=one_curse_number[3],
            callback_data=group_callback.new(group=one_curse_number[3])
        ),
        InlineKeyboardButton(
            text=one_curse_number[4],
            callback_data=group_callback.new(group=[one_curse_number[4]])
        ),
        InlineKeyboardButton(
            text=one_curse_number[5],
            callback_data=group_callback.new(group=one_curse_number[5])
        )
    ],
    [
        InlineKeyboardButton(
            text=one_curse_number[6],
            callback_data=group_callback.new(group=one_curse_number[6])
        ),
        InlineKeyboardButton(
            text=one_curse_number[7],
            callback_data=group_callback.new(group=one_curse_number[7])
        ),
        InlineKeyboardButton(
            text=one_curse_number[8],
            callback_data=group_callback.new(group=one_curse_number[8])
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data=Menu_nextback.new(nextback="level1")
        )
    ]

])

two_course = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(
            text=two_curse_number[0],
            callback_data=group_callback.new(group=two_curse_number[0])
        ),
        InlineKeyboardButton(
            text=two_curse_number[1],
            callback_data=group_callback.new(group=two_curse_number[1])
        ),
        InlineKeyboardButton(
            text=two_curse_number[2],
            callback_data=group_callback.new(group=two_curse_number[2])
        )
    ],
    [
        InlineKeyboardButton(
            text=two_curse_number[3],
            callback_data=group_callback.new(group=two_curse_number[3])
        ),
        InlineKeyboardButton(
            text=two_curse_number[5],
            callback_data=group_callback.new(group=two_curse_number[4])
        ),
        InlineKeyboardButton(
            text=two_curse_number[5],
            callback_data=group_callback.new(group=two_curse_number[5])
        )
    ],
    [
        InlineKeyboardButton(
            text=two_curse_number[6],
            callback_data=group_callback.new(group=two_curse_number[6])
        ),
        InlineKeyboardButton(
            text=two_curse_number[7],
            callback_data=group_callback.new(group=two_curse_number[7])
        ),
        InlineKeyboardButton(
            text=two_curse_number[8],
            callback_data=group_callback.new(group=two_curse_number[8])
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data=Menu_nextback.new(nextback="level1")
        )
    ]
])
three_course = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text=three_curse_number[0],
            callback_data=group_callback.new(group=three_curse_number[0])
        ),
        InlineKeyboardButton(
            text=three_curse_number[1],
            callback_data=group_callback.new(group=three_curse_number[1])
        )
    ],
    [
        InlineKeyboardButton(
            text=three_curse_number[2],
            callback_data=group_callback.new(group=three_curse_number[2])
        ),
        InlineKeyboardButton(
            text=three_curse_number[3],
            callback_data=group_callback.new(group=three_curse_number[3])
        )
    ],
    [
        InlineKeyboardButton(
            text=three_curse_number[4],
            callback_data=group_callback.new(group=one_curse_number[4])
        ),
        InlineKeyboardButton(
            text=three_curse_number[5],
            callback_data=group_callback.new(group=one_curse_number[5])
        )

    ],
    [
        InlineKeyboardButton(
            text=three_curse_number[6],
            callback_data=group_callback.new(group=three_curse_number[6])
        ),
        InlineKeyboardButton(
            text=three_curse_number[7],
            callback_data=group_callback.new(group=three_curse_number[7])
        )

    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data=Menu_nextback.new(nextback="level1")
        )
    ]

])

four_course = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text=four_curse_number[0],
            callback_data=group_callback.new(group=four_curse_number[0])
        ),
        InlineKeyboardButton(
            text=four_curse_number[1],
            callback_data=group_callback.new(group=four_curse_number[1])
        )
    ],
    [
        InlineKeyboardButton(
            text=four_curse_number[2],
            callback_data=group_callback.new(group=four_curse_number[2])
        ),
        InlineKeyboardButton(
            text=four_curse_number[3],
            callback_data=group_callback.new(group=four_curse_number[3])
        )
    ],
    [
        InlineKeyboardButton(
            text=four_curse_number[4],
            callback_data=group_callback.new(group=four_curse_number[4])
        ),
        InlineKeyboardButton(
            text=four_curse_number[5],
            callback_data=group_callback.new(group=four_curse_number[5])
        )

    ],
    [
        InlineKeyboardButton(
            text=four_curse_number[6],
            callback_data=group_callback.new(group=four_curse_number[6])
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data=Menu_nextback.new(nextback="level1")
        )
    ]

])

level1_keyboard = InlineKeyboardMarkup()
level1 = InlineKeyboardButton(text="Вернутсься до выбора курса", callback_data=Menu_callback.new(course="первый"))
level1_keyboard.insert(level1)
