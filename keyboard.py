from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from text import *





def kb_main():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=major, callback_data="main")
    return keyboard.as_markup()
