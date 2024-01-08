from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    ism_familiya = State()
    yosh = State()
    aloqa = State()
    hudud = State()
    Narx = State()
    murojaat = State()
    Maqsad = State()
    time = State()
    addmean = State()
