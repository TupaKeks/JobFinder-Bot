import json
import aiohttp
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from main import parse_jobs

TOKEN = "8101806901:AAHLEYE8bADwfPYAGWwkKCnbGtAnkgK46uU"
CHAT_ID = "874533571"
JOBS_FILE = "job_data.json"
SENT_JOBS_FILE = "sent_jobs.json"

bot = Bot(TOKEN)
dp = Dispatcher()

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📌 Choose City", callback_data="choose_city")],
    [InlineKeyboardButton(text="💼 Choose Category", callback_data="choose_category")],
    [InlineKeyboardButton(text="🔍 Start Searching", callback_data="start_search")]
])

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello! Welcome to the job search bot!", reply_markup=main_menu)

city_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Warszawa", callback_data="city_warszawa")],
    [InlineKeyboardButton(text="Kraków", callback_data="city_krakow")],
    [InlineKeyboardButton(text="Łódź", callback_data="city_lodz")],
    [InlineKeyboardButton(text="Poznań", callback_data="city_poznan")],
])

@dp.callback_query(lambda c: c.data == "choose_city")
async def choose_city(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, "Please choose a city:", reply_markup=city_menu)

category_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="IT-Administracja", callback_data="category_it-administracja")],
    [InlineKeyboardButton(text="IT-Oprogramowania", callback_data="category_it-oprogramowania")],
    [InlineKeyboardButton(text="Sprzedaż", callback_data="category_sprzedaż")],
    [InlineKeyboardButton(text="Inne", callback_data="category_inne")],
])

@dp.callback_query(lambda c: c.data == "choose_category")
async def choose_category(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, "Please choose a category:", reply_markup=category_menu)

user_choices = {}

@dp.callback_query(lambda c: c.data.startswith("city_"))
async def select_city(callback: CallbackQuery):
    user_choices[callback.from_user.id] = {"city": callback.data.replace("city_", "")}
    await bot.send_message(callback.from_user.id, f"City has been selected: {user_choices[callback.from_user.id]['city']}")

@dp.callback_query(lambda c: c.data.startswith("category_"))
async def select_category(callback: CallbackQuery):
    user_choices[callback.from_user.id]["category"] = callback.data.replace("category_", "")
    await bot.send_message(callback.from_user.id, f"Category has been selected: {user_choices[callback.from_user.id]['category']}")

@dp.callback_query(lambda c: c.data == "start_search")
async def start_search(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, "🔍 Начинаем поиск вакансий...")
    city = user_choices[callback.from_user.id]['city']
    category = user_choices[callback.from_user.id]['category']
    # ВАЖНО: теперь парсер запускается ТОЛЬКО при нажатии кнопки
    jobs = parse_jobs(city, category)  
    sent_jobs = load_sent_jobs()
    new_jobs = [job for job in jobs if job["url"] not in sent_jobs]

    for job in new_jobs:
        text = f"📌 <b>{job['title']}</b>\n🔗 [Ссылка]({job['url']})"
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Подробнее", url=job["url"])]
        ])
        await bot.send_message(CHAT_ID, text, parse_mode="HTML", reply_markup=keyboard)

    sent_jobs.extend([job["url"] for job in new_jobs])
    save_sent_jobs(sent_jobs)

def load_sent_jobs():
    try:
        with open(SENT_JOBS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_sent_jobs(jobs):
    with open(SENT_JOBS_FILE, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())