from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from api import get_hudud


hududMenu = InlineKeyboardMarkup(row_width=2)
for i in get_hudud():
    hududMenu.insert(InlineKeyboardButton(text=i['name'], callback_data=f"M{i['id']}"))
def b_button(tuman):
    tumanMenu = InlineKeyboardMarkup(row_width=2)
    for i in tuman:
        tumanMenu.insert(InlineKeyboardButton(text=f"{i['name']}({i['id']})", callback_data=f"T{i['id']}"))

    return tumanMenu

def all_pro(profil):
    promenu = InlineKeyboardMarkup(row_width=1)
    for i in profil:
        promenu.insert(InlineKeyboardButton(text=f"{i['fulname']} ({i['lavozim']})", callback_data=f"P{i['id']}"))

    return promenu