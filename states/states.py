from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    ism_familiya = State()
    yosh = State()
    aloqa = State()
    hudud = State()
    Narx = State()
    murojaat = State()
    time = State()
    addmean = State()

    ism_familiya_dasturlash = State()
    yosh_dasturlash = State()
    aloqa_dasturlash = State()
    hudud_dasturlash = State()
    Narx_dasturlash = State()
    murojaat_dasturlash = State()
    time_dasturlash = State()

    ism_familiya_savodxonlik = State()
    yosh_savodxonlik = State()
    aloqa_savodxonlik = State()
    hudud_savodxonlik = State()
    Narx_savodxonlik = State()
    murojaat_savodxonlik = State()
    time_savodxonlik = State()

    ism_familiya_ingliz = State()
    yosh_ingliz = State()
    aloqa_ingliz = State()
    hudud_ingliz = State()
    Narx_ingliz = State()
    murojaat_ingliz = State()
    time_ingliz = State()