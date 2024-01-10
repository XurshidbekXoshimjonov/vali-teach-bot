from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu, majburiy_obuna, table
from loader import bot, db
import sqlite3
from states.states import Form
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

savodxonlik_router: Router = Router()





@savodxonlik_router.message(F.text == "💻 Kompyuter savodxonligi")
async def f1(message: Message, state: FSMContext):
    await message.answer("Iltimos so'rovnomani to'ldiring!")
    await state.set_state(Form.ism_familiya_savodxonlik)
    await message.answer("✏️ Ism, familiyangizni kiriting?",)


@savodxonlik_router.message(Form.ism_familiya_savodxonlik)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya_savodxonlik=message.text)
    await state.set_state(Form.yosh_savodxonlik)
    await message.answer("👨🏼‍💼👩🏼‍💼 Yoshingiz?")

@savodxonlik_router.message(Form.yosh_savodxonlik)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(yosh_savodxonlik=message.text)
    await state.set_state(Form.hudud_savodxonlik)
    await message.answer("📍 Qaysi hududda yashaysiz?\n(Masalan: Farg'ona viloyati, Rishton tumani)")

@savodxonlik_router.message(Form.hudud_savodxonlik)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud_savodxonlik=message.text)
    await state.set_state(Form.aloqa_savodxonlik)
    await message.answer("📞 Telefon raqamingiz?")


@savodxonlik_router.message(Form.aloqa_savodxonlik)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa_savodxonlik=message.text)
    await state.set_state(Form.murojaat_savodxonlik)
    await message.answer("""⌚️ Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 8:00 - 20:00
""")
    
@savodxonlik_router.message(Form.murojaat_savodxonlik)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat_savodxonlik=message.text)    
    user = await state.get_data()
    await state.clear()
  

    await message.answer(f"Buyurtma:\n 📚Kurs: 💻#Kompyutersavodxonligi\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya_savodxonlik']}\n 👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh_savodxonlik']}\n 📍 Yashash joyi: {user['hudud_savodxonlik']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa_savodxonlik']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat_savodxonlik']}\n")

    await bot.send_message(chat_id="5626949720", text=f"Buyurtma:\n 📚Kurs:💻#Kompyutersavodxonligi\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya_savodxonlik']}\n  👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh_savodxonlik']}\n 📍 Yashash joyi: {user['hudud_savodxonlik']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa_savodxonlik']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat_savodxonlik']}\n")
   


