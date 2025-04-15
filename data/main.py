from aiogram import Bot, Dispatcher, executor, types
from db import create_pool
import logging
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",  # или None, если только консоль
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

load_dotenv()

API_TOKEN = os.getenv("7660783997:AAEWRRd6KMYA-BThWlO26LIz0LQ0Qyh50ug")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("🧞 Я Джин. Одно желание. Если не про пенсию — стебаюсь.")

async def on_startup(dp):
    dp.pool = await create_pool()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
