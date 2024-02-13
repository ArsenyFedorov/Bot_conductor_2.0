from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from text import *
import datetime


class SimpleCallback(CallbackData, prefix="scb"):
    callback: str = ""
    date: datetime


def kb_main(date_day: datetime):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=accept, callback_data=SimpleCallback(callback="accept", date=date_day))
    keyboard.button(text=reject, callback_data=SimpleCallback(callback="reject", date=date_day))
    return keyboard.as_markup()





