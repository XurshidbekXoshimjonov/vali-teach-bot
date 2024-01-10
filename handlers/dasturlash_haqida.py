from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu, majburiy_obuna, table, course, checking
from loader import bot, db
import sqlite3
from states.states import Form
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

dasturlash_router: Router = Router()

@dasturlash_router.message(F.text == "Kurslar haqida")
async def dasturlash(message: Message):
    await message.answer("Kurslarni tanlang!", reply_markup=course)




@dasturlash_router.message(F.text == "👨‍💻 Dasturlash haqida")
async def dasturlash1(message: Message, state: FSMContext):
    await message.answer("📚Kurs: 👨‍💻 #Dasturlash\n 🕔Kurs muddati: 1 yil\n 💰To'lov summa: 390 000 so'm\n Dasturlar: Visual Studio Code\n O'rgatiladigan dasturlash tillari: Html, Css, Scss, Bootstrap, JavaScript, Python, Telegram bot, Django\nMaslahat: Dasturlash kursida o'qish uchun o'zingizning shaxsiy noutbukingizga ega bo'lishingiz kerak(Majburiy emas!)")
    await message.answer("Ro'yhatdan o'tish uchun tugmani bosing", reply_markup=checking)

@dasturlash_router.callback_query(F.data=="check")
async def check(message: CallbackQuery):
    await message.answer("Kurslarni tanlang!", reply_markup=menu)