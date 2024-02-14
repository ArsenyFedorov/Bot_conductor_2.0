from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from text import *
import datetime


class SimpleCallback(CallbackData, prefix="scb"):
    callback: str = ""
    status: str = ""
    date: str = ""


def kb_main(day: datetime):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=accept, callback_data=SimpleCallback(callback="edit", status=accept, date=str(day)))
    keyboard.button(text=reject, callback_data=SimpleCallback(callback="edit", status=reject, date=str(day)))
    return keyboard.as_markup()
