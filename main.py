from aiogram import Dispatcher, Bot
import os
import asyncio
from handlers import *
from data_base.record import Record
from data_base.user import User

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(handlers_router)


def on_start():
    print("Bot запущен")
    print("База данных", end=" ")
    try:
        Record.great_table()
        print("Подключено", end=" ")
        User.great_table()
        print("И эта тоже")
    except:
        print("Не подключено")


async def start_bot():
    dp.startup.register(on_start)
    # Пока бот выключен все запросы удаляются
    await bot.delete_webhook(drop_pending_updates=True)
    # бот сам проверяет запросы
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
