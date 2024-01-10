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

ingliz_tili_haqida_router: Router = Router()

@ingliz_tili_haqida_router.message(F.text == "Kurslar haqida")
async def fghjk(message: Message):
    await message.answer("Kurslarni tanlang!", reply_markup=course)




@ingliz_tili_haqida_router.message(F.text == "🇬🇧 Ingliz tili haqida")
async def fghjk(message: Message, state: FSMContext):
    await message.answer("📚Kurs: 👨‍💻#Ingliztili\n 🕔Kurs muddati: 1-2 yil\n 💰To'lov summa: 260 000 so'm\n Sertifikatlar: IELTS(7+), CEFR\n")
    await message.answer("Ro'yhatdan o'tish uchun tugmani bosing", reply_markup=checking)

@ingliz_tili_haqida_router.callback_query(F.data=="check")
async def check(message: CallbackQuery):
    await message.answer("Kurslarni tanlang!", reply_markup=menu)