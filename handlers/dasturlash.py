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



@programming_router.message(F.text == "👨‍💻Dasturlash")
async def f1(message: Message, state: FSMContext):
    await message.answer("Iltimos so'rovnomani to'ldiring!")
    await state.set_state(Form.ism_familiya_dasturlash)
    await message.answer("✏️ Ism, familiyangizni kiriting?",)


@programming_router.message(Form.ism_familiya_dasturlash)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(ism_familiya_dasturlash=message.text)
    await state.set_state(Form.yosh_dasturlash)
    await message.answer("👨🏼‍💼👩🏼‍💼 Yoshingiz?")

@programming_router.message(Form.yosh_dasturlash)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(yosh_dasturlash=message.text)
    await state.set_state(Form.hudud_dasturlash)
    await message.answer("📍 Qaysi hududda yashaysiz?\n(Masalan: Farg'ona viloyati, Rishton tumani)")

@programming_router.message(Form.hudud_dasturlash)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(hudud_dasturlash=message.text)
    await state.set_state(Form.aloqa_dasturlash)
    await message.answer("📞 Telefon raqamingiz?")


@programming_router.message(Form.aloqa_dasturlash)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(aloqa_dasturlash=message.text)
    await state.set_state(Form.murojaat_dasturlash)
    await message.answer("""⌚️ Murojaat qilish vaqti\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00\n""")
    
@programming_router.message(Form.murojaat_dasturlash)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(murojaat_dasturlash=message.text)    
    user = await state.get_data()
    await state.clear()
  

    await message.answer(f"Buyurtma:\n 📚Kurs: 👨‍💻#Dasturlash\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya_dasturlash']}\n 👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh_dasturlash']}\n 📍 Yashash joyi: {user['hudud_dasturlash']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa_dasturlash']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat_dasturlash']}\n")

    await bot.send_message(chat_id="5626949720", text=f"Buyurtma:\n 📚Kurs: 👨‍💻#Dasturlash\n 👨‍🎓🧑‍🎓Mijoz: {user['ism_familiya_dasturlash']}\n 👨🏼‍💼👩🏼‍💼 Yoshi: {user['yosh_dasturlash']}\n 📍 Yashash joyi: {user['hudud_dasturlash']}\n 🇺🇿  Telegram: @{message.from_user.username} \n  📞 Telefon raqami: {user['aloqa_dasturlash']}\n ⌚️ Murojaat qilish vaqti:{user['murojaat_dasturlash']}\n")
   


