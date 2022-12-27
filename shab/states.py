from aiogram.dispatcher.filters.state import State,StatesGroup


class ProfilState(StatesGroup):
    fullname = State()
    lavozim = State()
    tel = State()
    shahar = State()