import os
from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command

from async_update import get_notification_urls

load_dotenv('.env')

TG_API = os.getenv('TG_TOKEN')

async def bot_config():
    global TG_API

    bot = Bot(token=TG_API)
    dp = Dispatcher()
    router = Router()

    @router.message(Command('start'))
    async def send_welcome(message):
        await bot.send_message(message.chat.id, 'hi')


    @router.message(Command('notific'))
    async def send_site_link(message):
        try:
            notification_urls = await get_notification_urls()

            id_ = int(message.text.split()[1])
            if id_ in notification_urls:
                await bot.send_message(message.chat.id, f'Сайт {notification_urls[id_]} доступен для посещения')
        except Exception:
            pass


    dp.include_router(router)
    await dp.start_polling(bot)

def start_bot():
    asyncio.run(bot_config())