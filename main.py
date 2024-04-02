import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor
from pathlib import Path
import threading
from subprocess import call
import os, errno
import shutil



API_TOKEN = '6098270691:AAFM11zcagxwHlDyWmAgrkYMn5p189kDayU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
admin_id = 1370770852
k = 0

# Устанавливаем соединение с базой данных SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
# Создаем таблицу, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    name TEXT,
                    description TEXT,
                    photo BLOB,
                    kolvo TEXT ''
                )''')
conn.commit()



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id == admin_id:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Хочу бонус!"))
        await message.answer("Опции администратора", reply_markup=keyboard)

@dp.message_handler(text=['Добавить товар'])
async def start(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Введите наименование товара")

@dp.message_handler()
async def start(message: types.Message):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
