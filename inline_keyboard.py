from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_WEATHER = InlineKeyboardButton(text="Weather", callback_data="weather")
BTN_WIND = InlineKeyboardButton(text="Wind", callback_data="wind")
BTN_SUN_TIME = InlineKeyboardButton(text="Sunrise and sunset", callback_data="sun_time")

WEATHER = InlineKeyboardMarkup(inline_keyboard=[[BTN_WIND, BTN_SUN_TIME]])
WIND = InlineKeyboardMarkup(inline_keyboard=[[BTN_WEATHER, BTN_SUN_TIME]])
SUN_TIME = InlineKeyboardMarkup(inline_keyboard=[[BTN_WEATHER, BTN_WIND]])
HELP = InlineKeyboardMarkup(inline_keyboard=[[BTN_WEATHER, BTN_WIND, BTN_SUN_TIME]])
