from aiogram import Router, F, Bot, types
from aiogram.types import Message, CallbackQuery, InputFile, InputMediaPhoto
from aiogram.filters import Command
from data_base.user import User
from aiogram.filters.callback_data import CallbackData
from keyboard import *
from text import *
from data_base.record import Record
import datetime
import aioschedule
import asyncio

handlers_router = Router()


@handlers_router.message(Command("start"))
async def com_start(message: Message, bot: Bot):
    record = Record()
    user = User(message.from_user.id)
    if user.user:
        records_list = list(record.load(tg_id=message.from_user.id))
        if records_list:
            new_records_list = []
            for records in records_list:
                current_date = datetime.date.today()
                date_records = list(records)[3].split("-")
                date_records = datetime.date(int(date_records[0]), int(date_records[1]), int(date_records[2]))
                if current_date >= date_records:
                    continue
                else:
                    new_records_list.append(date_records)
            await check_date(message=message, bot=bot, date=new_records_list)
        else:
            await bot.send_message(text="IDINAXYI2", chat_id=message.chat.id)
    else:
        await bot.send_message(text="IDI NAXYI", chat_id=message.chat.id)


async def check_date(message: types.Message, bot: Bot, date: list):
    while date:
        now = datetime.date.today()
        copy_date = date
        for day in copy_date:
            if (now - day).days == -1:
                await bot.send_message(chat_id=message.chat.id, text=choice,
                                       reply_markup=kb_main(day))
                date.remove(day)
        await asyncio.sleep(86400)


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "edit"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    record = Record()
    status = callback_data.status
    date = callback_data.date.split("-")
    date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    record.save(date=date, status=status)
    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        text=happily)
