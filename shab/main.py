from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from states import ProfilState
import logging
from button import *
from inlinebutton import *
from aiogram import Bot, Dispatcher, executor, types
from api import *
from aiogram.dispatcher import FSMContext




API_TOKEN = '5900937218:AAFiCI0WjFkajoBGw8xcUA-VBZSt57JrTuE'
ADMINS = ["1777781933"]
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if str(message.chat.id) in ADMINS:
        await message.answer("Assalomu alaykum!\nSmart botimizga!\nXush kelibsiz.",reply_markup=hududlar)
    elif get_profil(user_id=message.from_user.id) is None:
        await message.answer("Assalomu alaykum!\nSmart botimizga!\nXush kelibsiz.", reply_markup=create_profil)
        create_user(message.from_user.username,message.from_user.first_name,message.from_user.id)
    else:
        ism = get_profil(user_id=message.from_user.id)
        await message.answer(f"Assalomu alaykum!\n{ism}\nProfilingizga kirishingiz mumkin.", reply_markup=kirish)




@dp.message_handler(text = "Hududlar", user_id = ADMINS)
async def admin_hudud(message: types.Message):
    await message.answer(f"Hududlardan birini tanlang",reply_markup=hududMenu)
    await message.delete()



@dp.callback_query_handler(Text(startswith="M"), user_id = ADMINS)
async def buy_books(call: CallbackQuery):
    murkap = b_button(get_shahar(int(call['data'][-1:])))
    await call.message.answer("Tumanlarni tanlang.", reply_markup=murkap)
    await call.message.delete()


@dp.callback_query_handler(Text(startswith="T"), user_id = ADMINS)
async def buy_books(call: CallbackQuery):
    probut = all_pro(all_profil(int(call['data'][-1:])))
    await call.message.answer("Tanlang👇",reply_markup=probut)
    await call.message.delete()



@dp.message_handler(text = "Profil yaratish")
async def holat_1(message: types.Message):
    await message.answer("Ism Familiya va Sharifingizni to'liq yozing!\nMasalan: (Olimjon Baxodirov Karimjonovich)")
    await ProfilState.fullname.set()

@dp.message_handler(state=ProfilState.fullname)
async def holat_2(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(name = fullname)
    await message.answer("Lavozimingizni kiriting!")
    await ProfilState.next()

@dp.message_handler(state=ProfilState.lavozim)
async def holat_3(message: types.Message, state: FSMContext):
    lavozim = message.text
    await state.update_data(lavozim=lavozim)
    await message.answer("Telefon raqamni yuboring!", reply_markup=telefon)
    await ProfilState.next()


@dp.message_handler(state=ProfilState.tel, content_types="contact")
async def holat_4(message: types.Message, state: FSMContext):
    tel = message.contact.phone_number
    await state.update_data(tel=tel)
    await message.answer("Viloyatni tanlang.👇", reply_markup=hududMenu)
    await ProfilState.next()


@dp.callback_query_handler(Text(startswith="M"),state=ProfilState.shahar)
async def buy_book(call: CallbackQuery, state: FSMContext):
    murkap = b_button(get_shahar(int(call['data'][-1:])))
    await call.message.answer("Tumanni tanlang.👇", reply_markup=murkap)
    await call.message.delete()

@dp.callback_query_handler(Text(startswith="T"),state=ProfilState.shahar)
async def buy_boo(call: CallbackQuery,state: FSMContext):
    shahar = int(call['data'][-1:])
    data = await state.get_data()
    fullname = data.get("name")
    lavozim = data.get("lavozim")
    tel = data.get("tel")
    Create_profil(fullname=fullname,lavozim=lavozim,tel=str(tel), user_id=call.from_user.id,shahar=shahar)
    await call.message.answer("Profil yaratildi.👇", reply_markup=kirish)
    await state.finish()
    await call.message.delete()




@dp.message_handler(text = "Profilga kirish")
async def profil(message: types.Message):
    a = get_profil(user_id=message.from_user.id)

    await message.answer(f"{a}", reply_markup=qilingan)










if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)