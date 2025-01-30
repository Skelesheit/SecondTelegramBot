import asyncio

from aiogram import Bot, Dispatcher
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage

from config.config import load_config, TelegramBotConfig
from src import handlers

bot_config = load_config()
token = bot_config.token
bot = Bot(token=token)


redis_client = Redis(host=bot_config.host, port=bot_config.port, db=0, decode_responses=True)

storage = RedisStorage(redis_client)

dp = Dispatcher(storage=storage)
dp.include_router(handlers.router)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())