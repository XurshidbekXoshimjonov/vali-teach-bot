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