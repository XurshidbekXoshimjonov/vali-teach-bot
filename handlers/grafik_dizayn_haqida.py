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

about_graphic_design_router: Router = Router()

@about_graphic_design_router.message(F.text == "Kurslar haqida")
async def fghjk(message: Message):
    await message.answer("Kurslarni tanlang!", reply_markup=course)




@about_graphic_design_router.message(F.text == "💡Grafik dizayn haqida")
async def fghjk(message: Message, state: FSMContext):
    await message.answer("📚Kurs: 👨‍💻Grafik dizayn\n 🕔Kurs muddati: 5 oy\n 💰To'lov summa: 440 000 so'm\n Dasturlar: Adobe Photoshop, Adobe Illustrator, Corel Draw\n Maslahat: Grafik dizayn kursida o'qish uchun o'zingizning shaxsiy noutbukingizga ega bo'lishingiz kerak(Majburiy emas!)")
    await message.answer("Ro'yhatdan o'tish uchun tugmani bosing", reply_markup=checking)

@about_graphic_design_router.callback_query(F.data=="check")
async def check(message: CallbackQuery):
    await message.answer("Kurslarni tanlang!", reply_markup=menu)