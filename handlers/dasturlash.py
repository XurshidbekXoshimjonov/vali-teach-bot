from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu, majburiy_obuna, table
from loader import bot, db
import sqlite3
from states.states import Form
from aiogram.fsm.context import FSMContext

programming_router: Router = Router()


@programming_router.message(F.text == "👨‍💻 Dasturlash")
@programming_router.message(F.text == "👨‍💻 Dasturlash haqida")
@programming_router.message(F.text == "🇬🇧 Ingliz tili haqida")
@programming_router.message(F.text == "🇬🇧 Ingliz tili")
@programming_router.message(F.text == "💻 Kompyuter savodxonligi")
@programming_router.message(F.text == "💻 Kompyuter savodxonligi haqida")
@programming_router.message(F.text == "💻 Kompyuter savodxonligi haqida")
@programming_router.message(F.text == "O'quv markaz haqida")
async def mjng(message: Message):
    await message.answer("Kechirasiz, Hozircha bu bo'lim ishlamaydi, yaqin kunlarda bu bo'lim ham ishga tushuriladi!😉", reply_markup=menu)