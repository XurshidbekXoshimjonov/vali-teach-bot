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

savodxonlik_haqida_router: Router = Router()

@savodxonlik_haqida_router.message(F.text == "Kurslar haqida")
async def fghjk(message: Message):
    await message.answer("Kurslarni tanlang!", reply_markup=course)




@savodxonlik_haqida_router.message(F.text == "💻 Kompyuter savodxonligi haqida")
async def fghjk(message: Message, state: FSMContext):
    await message.answer("📚Kurs: #Kompyutersavodxonligi\n 🕔Kurs muddati: 1 oy\n 💰To'lov summa: 260 000 so'm\n Dasturlar: Microsoft Office dasturlari. Maslahat: Kompyuter savodxonligida o`qishingiz uchun shaxsiy kompyuteringiz bo`lishi shart emas!  ")
    await message.answer("Ro'yhatdan o'tish uchun tugmani bosing", reply_markup=checking)

@savodxonlik_haqida_router.callback_query(F.data=="check")
async def check(message: CallbackQuery):
    await message.answer("Kurslarni tanlang!", reply_markup=menu)