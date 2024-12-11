import asyncio

from aiogram import Bot, Dispatcher
from config.config import load_config, TelegramBotConfig
from src import handlers

bot_config = load_config()
token = bot_config.token
bot = Bot(token=token)

dp = Dispatcher()
dp.include_router(handlers.router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())