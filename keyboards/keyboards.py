from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text="💡 Grafik dizayn"),
                KeyboardButton(text="👨‍💻Dasturlash")
            ],
            [
                KeyboardButton(text="🇬🇧 Ingliz tili"),
                KeyboardButton(text="💻 Kompyuter savodxonligi")
            ],
             [
                KeyboardButton(text="🔙Orqaga"),
                KeyboardButton(text="Asosiy menyu")
            ]
    ],
            resize_keyboard=True
    )

table = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text="Ro'yxatdan o'tish"),
                KeyboardButton(text="Kurslar haqida")
            ],
            [
                KeyboardButton(text="O'quv markaz haqida")
            ]
    ],
            resize_keyboard=True
    )




majburiy_obuna = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-kanal", url="https://t.me/Vali_Teach_Kokand")
        ],
        [
            InlineKeyboardButton(text="2-kanal", url="https://t.me/valiteach_natijalar")
        ],
        [
            InlineKeyboardButton(text="3-kanal", url="https://t.me/valiteach_oqjar")
        ],
        [
            InlineKeyboardButton(text="Tasdiqlash",callback_data="tasdiqlash")
        ]
    ]
)


course = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text="💡Grafik dizayn haqida"),
                KeyboardButton(text="👨‍💻 Dasturlash haqida")
            ],
            [
                KeyboardButton(text="🇬🇧 Ingliz tili haqida"),
               KeyboardButton(text="💻 Kompyuter savodxonligi haqida")
            ],
             [
                KeyboardButton(text="🔙Orqaga"),
                KeyboardButton(text="Asosiy menyu")
            ]
    ],
            resize_keyboard=True
    )
checking = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="check")
        ],
    ]
)