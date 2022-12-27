from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hududlar = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Hududlar')
        ],
    ],
    resize_keyboard=True
)

telefon = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📲 Contact', request_contact=True)
        ],
    ],
    resize_keyboard=True
)

create_profil = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Profil yaratish')
        ],
    ],
    resize_keyboard=True
)


kirish = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Profilga kirish')
        ],
    ],
    resize_keyboard=True
)

qilingan = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Ma'lumot yuborish")
        ],
    ],
    resize_keyboard=True
)