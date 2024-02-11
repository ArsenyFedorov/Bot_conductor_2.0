from aiogram import Router, F, Bot, types
from aiogram.types import Message, CallbackQuery, InputFile, InputMediaPhoto
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from keyboard import *
from text import *
from data_base.record import Record
import datetime

handlers_router = Router()


@handlers_router.message(Command("start"))
async def com_start(message: Message, bot: Bot):
    pass








