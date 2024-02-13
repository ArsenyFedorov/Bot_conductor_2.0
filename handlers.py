from aiogram import Router, F, Bot, types
from aiogram.types import Message, CallbackQuery, InputFile, InputMediaPhoto
from aiogram.filters import Command
from data_base.user import User
from aiogram.filters.callback_data import CallbackData
from keyboard import *
from text import *
from data_base.record import Record
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

handlers_router = Router()


@handlers_router.message(Command("start"))
async def com_start(message: Message, bot: Bot):
    record = Record()
    record.create(tg_id=message.from_user.id, date=datetime.date(2024, 11, 26), name="Арсений", status="Не подтверждён")
    user = User(message.from_user.id)
    if user.user:
        records_list = list(record.load(tg_id=message.from_user.id))
        if records_list:
            for records in records_list:
                current_date = datetime.date.today()
                date_records = list(records)[3].split("-")
                date_records = datetime.date(int(date_records[0]), int(date_records[1]), int(date_records[2]))
                if current_date >= date_records:
                    continue
                else:
                    await bot.send_message(text="IDI NAXYI3", chat_id=message.chat.id,
                                           reply_markup=kb_main(date_records))
        else:
            await bot.send_message(text="IDINAXYI2", chat_id=message.chat.id)
    else:
        await bot.send_message(text="IDI NAXYI", chat_id=message.chat.id)


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "accetp"))
async def accept(callback_data: SimpleCallback):
    day = callback_data.date
    status = "Подтвержённо"
    record = Record()
    record.save(data=day, status=status)


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "reject"))
def reject(callback_data: SimpleCallback):
    day = callback_data.date
    status = "Отклонено"
    record = Record()
    record.save(data=day, status=status)




