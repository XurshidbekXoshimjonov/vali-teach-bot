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

ingliz_tili_router: Router = Router()





@ingliz_tili_router.message(F.text == "🇬🇧 Ingliz tili")
async def jhyt(message: Message, state: FSMContext):
    await message.answer("Iltimos so'rovnomani to'ldiring!")
    await state.set_state(Form.ism_familiya_ingliz)
    await message.answer("✏️ Ism, familiyangizni kiriting?",)


@ingliz_tili_router.message(Form.ism_familiya_ingliz)
async def  jhyt(message: Message, state: FSMContext):
    await state.update_data(ism_familiya_ingliz=message.text)
    await state.set_state(Form.yosh_ingliz)
    await message.answer("👨🏼‍💼👩🏼‍💼 Yoshingiz?")

@ingliz_tili_router.message(Form.yosh_ingliz)
async def  jhyt(message: Message, state: FSMContext):
    await state.update_data(yosh_ingliz=message.text)
    await state.set_state(Form.hudud_ingliz)
    await message.answer("📍 Qaysi hududda yashaysiz?\n(Masalan: Farg'ona viloyati, Rishton tumani)")

@ingliz_tili_router.message(Form.hudud_ingliz)
async def  jhyt(message: Message, state: FSMContext):
    await state.update_data(hudud_ingliz=message.text)
    await state.set_state(Form.aloqa_ingliz)
    await message.answer("📞 Telefon raqamingiz?")


@ingliz_tili_router.message(Form.aloqa_ingliz)
async def  jhyt(message: Message, state: FSMContext):
    await state.update_data(aloqa_ingliz=message.text)
    await state.set_state(Form.murojaat_ingliz)
    await message.answer("""⌚️ Murojaat qilish vaqti:\n 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
""")
    
@ingliz_tili_router.message(Form.murojaat_ingliz)
async def  jhyt(message: Message, state: FSMContext):
    await state.update_data(murojaat_ingliz=message.text)    
    user = await state.get_data()
    await state.clear()
  

    await message.answer(f"Buyurtma:\n 📚Kurs: 👨‍💻#Ingliztili\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya_ingliz']}\n 👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh_ingliz']}\n 📍 Yashash joyi: {user['hudud_ingliz']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa_ingliz']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat_ingliz']}\n")

    await bot.send_message(chat_id="5626949720", text=f"Buyurtma:\n 📚Kurs: 👨‍💻#Ingliztili\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya_ingliz']}\n  👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh_ingliz']}\n 📍 Yashash joyi: {user['hudud_ingliz']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa_ingliz']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat_ingliz']}\n")
   


