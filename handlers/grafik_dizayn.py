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

graphic_design_router: Router = Router()





@graphic_design_router.message(F.text == "💡 Grafik dizayn")
async def f1(message: Message, state: FSMContext):
    await message.answer("Iltimos so'rovnomani to'ldiring!")
    await state.set_state(Form.ism_familiya)
    await message.answer("✏️ Ism, familiyangizni kiriting?",)


@graphic_design_router.message(Form.ism_familiya)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya=message.text)
    await state.set_state(Form.yosh)
    await message.answer("👨🏼‍💼👩🏼‍💼 Yoshingiz?")

@graphic_design_router.message(Form.yosh)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await state.set_state(Form.hudud)
    await message.answer("📍 Qaysi hududda yashaysiz?\n(Masalan: Farg'ona shahri, Rishton tumani)")

@graphic_design_router.message(Form.hudud)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("📞 Telefon raqamingiz?")


@graphic_design_router.message(Form.aloqa)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.murojaat)
    await message.answer("""⌚️ Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")
    
@graphic_design_router.message(Form.murojaat)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat=message.text)    
    user = await state.get_data()
    await state.clear()
  

    await message.answer(f"Buyurtma:\n 📚Kurs: 👨‍💻#Grafikdizayn\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya']}\n 👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh']}\n 📍 Yashash joyi: {user['hudud']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat']}\n")

    await bot.send_message(chat_id="5626949720", text=f"Buyurtma:\n 📚Kurs: 👨‍💻#Grafikdizayn\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya']}\n  👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh']}\n 📍 Yashash joyi: {user['hudud']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat']}\n")
   


