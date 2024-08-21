import logging, asyncio

from aiogram import F, Bot, Dispatcher, types

# from aiogram.filters import callback_data
import inline_keyboard
import messages
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher()


@dp.message(F.text.lower().in_(["/start", "/weather"]))
async def handle_weather_command(message: types.Message):
    """
    Handle the 'start' and 'weather' commands.

    Args:
        message (types.Message): The incoming message.
    """
    weather_message = await messages.weather()
    await message.answer(text=weather_message, reply_markup=inline_keyboard.WEATHER)


@dp.message(F.text == "/help")
async def show_help_message(message: types.Message):
    await message.answer(
        text=f"This bot can get the current weather from your IP address.",
        reply_markup=inline_keyboard.HELP,
    )


@dp.message(F.text == "wind")
async def show_wind(message: types.Message):
    await message.answer(text=await messages.wind(), reply_markup=inline_keyboard.WIND)


@dp.message(F.text == "sun_time")
async def show_sun_time(message: types.Message):
    await message.answer(
        text=await messages.sun_time(), reply_markup=inline_keyboard.SUN_TIME
    )


@dp.callback_query(F.data == "weather")
async def process_callback_weather(callback_query: types.CallbackQuery):
    await callback_query.answer(
        text=await messages.weather(), show_alert=True, cache_time=config.CACHE_TIME
    )


@dp.callback_query(F.data == "wind")
async def process_callback_wind(callback_query: types.CallbackQuery):
    await callback_query.answer(
        text=await messages.wind(), show_alert=True, cache_time=config.CACHE_TIME
    )


@dp.callback_query(F.data == "sun_time")
async def process_callback_sun_time(callback_query: types.CallbackQuery):
    await callback_query.answer(
        text=await messages.sun_time(), show_alert=True, cache_time=config.CACHE_TIME
    )


async def main_():
    # Запуск LongPoll
    dp.run_polling(bot)


# asyncio.run(main_())
dp.run_polling(bot)
