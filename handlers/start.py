from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import majburiy_obuna, menu, table
from loader import db, bot
import sqlite3
start_router: Router = Router()





@start_router.message(Command("start"))
async def start(message: Message):
    await message.answer("Vali-Teach o'quv markazining qabul botiga xush kelibsiz!😊")
    await message.answer("""Birinchi bo'lib kanallarimizga obuna bo'ling""", reply_markup=table)
    








@start_router.callback_query(F.data=="tasdiqlash")
async def check(query: CallbackQuery):
    user = await GetChatMember(chat_id='-1001864241545', user_id=query.from_user.id)
    
    if user.status == "creator" :
        await bot.send_message(chat_id=query.from_user.id, text="Kanalga obuna bo'ldingiz, endi botdan foydalana olasiz! Tugmani tanlang",reply_markup=table)
    elif user.status == "admin":
         await bot.send_message(chat_id=query.from_user.id, text="Kanalga obuna bo'ldingiz, endi botdan foydalana olasiz! Tugmani tanlang",reply_markup=table)


    elif user.status == "member":
         await bot.send_message(chat_id=query.from_user.id, text="Kanalga obuna bo'ldingiz, endi botdan foydalana olasiz! Tugmani tanlang",reply_markup=table)
    else : 
        await bot.send_message(chat_id=query.from_user.id, text="Kechirasiz, agar siz kanalga obuna bo'lmagan bo'lsangiz botdan to'liq foydalana olmaysiz!")



