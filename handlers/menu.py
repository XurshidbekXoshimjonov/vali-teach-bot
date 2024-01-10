from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu, majburiy_obuna, table
from loader import bot, db
import sqlite3
from states.states import Form
from aiogram.fsm.context import FSMContext

menu_router: Router = Router()


@menu_router.message(F.text == "Ro'yxatdan o'tish")
async def mjng(message: Message):
    await message.answer("Kurslarni tanlang!", reply_markup=menu)




@menu_router.message(F.text == "🔙Orqaga")
@menu_router.message(F.text == "Asosiy menyu")
async def mjng(message: Message):
    await message.answer("Asosiy Menyu", reply_markup=table)

@menu_router.message(Command("help"))
async def start(message: Message):
    await message.answer("Assalomu alaykum sizga qanday yordam bera olaman?\nAgar botda kamchilik yoki noqulaylik sezsangiz Bot admini @Xoshim0ff ga murojaat qiling!")

@menu_router.message(Command("admin"))
async def f1(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum siz admin bilan bog'lanish tugmasini bosdingiz!")
    await state.set_state(Form.addmean)
    await message.answer("✏️ Savol yoki takliflaringiz bo'lsa shu yerga yuboring\nSavol yoki takliflaringiz Vali-Teach o'quv markazining adminstrator profiliga yuboriladi!")

@menu_router.message(Form.addmean)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(addmean=message.text)    
    user = await state.get_data()
    await state.clear()
  

    await message.answer(f"Savol va Taklif: {user['addmean']}\n 👨‍💻 Murojaatchi: @{message.from_user.username}")

    await bot.send_message(chat_id="5626949720", text=f"Savol va Taklif: {user['addmean']}\n👨‍💻 Murojaatchi: @{message.from_user.username}")
   


@menu_router.message(F.text == "O'quv markaz haqida")
async def mjng(message: Message):
    await message.answer("Kechirasiz, Hozircha bu bo'lim ishlamaydi, yaqin kunlarda bu bo'lim ham ishga tushuriladi!😉", reply_markup=menu)