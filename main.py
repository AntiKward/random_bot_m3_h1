from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import random
import asyncio
from config import token

bot = Bot(token=token)
dp = Dispatcher()

secret_number = 0

@dp.message(Command("start"))
async def start(message: Message):
    global secret_number
    secret_number = random.randint(1, 3)
    await message.answer("Я выбрал число от 1 до 3. Попробуйте угадать!")

@dp.message()
async def guess_number(message: Message):
    global secret_number
    try:
        user_numb = int(message.text)
        if user_numb == secret_number:
            await message.answer("Правильно! Вы отгадали!")
            await message.answer_photo("AgACAgIAAxkBAANUZzW90bhe8DWiIOaUq6FQh5XDeiUAAvDmMRvqJqhJl5_xtH1E1JYBAAMCAAN4AAM2BA")
            secret_number = random.randint(1, 3)
            await message.answer("Я снова загадал число от 1 до 3. Попробуйте угадать!")
        else:
            await message.answer("Неправильно. Попробуйте угадать еще раз!")
            await message.answer_photo("AgACAgIAAxkBAANVZzW-ZeoUJOBx2d4WQUmsdw4fqOwAAvvmMRvqJqhJHTgK7UjHQBsBAAMCAAN4AAM2BA")
    except ValueError:
        await message.answer("Пожалуйста, введите число от 1 до 3.")

async def main():
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Вы отключились от бота!")
