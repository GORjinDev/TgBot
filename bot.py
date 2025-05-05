import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command


TOKEN = '8199451521:AAG354ucQXPC-B4OWerDSDvbBekL4nfpknk'

bot = Bot(token=TOKEN)
dp = Dispatcher()

compliments = [
    "Я невероятно рад что узнал тебя, и ты у меня есть🥺",
    "Безумно люблю твою улыбку, и смех☺️",
    "Ты самая красивая девушка в которой мне нравится абсолютно все, каждый твой изгиб🥰",
]

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Start")],
    ],
    resize_keyboard=True
)

keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💖 Комплимент"), KeyboardButton(text="😑 Подвох?"), KeyboardButton(text="😏 Жопка")]
    ],
    resize_keyboard=True
)

# Обработчик для кнопки "Start"
@dp.message(lambda message: message.text == "Start")
async def start_button_handler(message: types.Message):
    await message.answer("Привет милая, хочу тебе кое-что сказать, нажми снизу кнопки ❤️", reply_markup=keyboard_main)

# Обработчик для комплимента
@dp.message(lambda message: message.text == "💖 Комплимент")
async def compliment_handler(message: types.Message):
    compliment = random.choice(compliments)
    await message.answer(compliment, reply_markup=keyboard_main)

# Обработчик для "Подвох?"
@dp.message(lambda message: message.text == "😑 Подвох?")
async def podvoh_handler(message: types.Message):
    await message.answer("Если все получится, я всегда буду рядом с тобой и не дам тебя обижать, а то теплое отношение которое есть к тебе, никуда не денется, и я всегда буду тебя ценить и любить ❤️", reply_markup=keyboard_main)

# Обработчик для "Жопка"
@dp.message(lambda message: message.text == "😏 Жопка")
async def zhopka_handler(message: types.Message):
    await message.answer("Ты моя любимая жопка 🙃", reply_markup=keyboard_main)

# Обработчик для команды /start (если пользователь не нажал Start)
@dp.message(Command('start'))
async def start_message_handler(message: types.Message):
    await message.answer("Нажми еще раз Start", reply_markup=keyboard_start)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
