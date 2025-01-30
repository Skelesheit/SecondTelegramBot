import os
from dotenv import load_dotenv
from pydantic import BaseModel


class TelegramBotConfig(BaseModel):
    token: str
    port: int
    host:  str

def load_config() -> TelegramBotConfig:
    """

    :rtype: object
    """
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
    token =  os.getenv("TELEGRAM_BOT_TOKEN")
    port = int(os.getenv("PORT"))
    host = os.getenv("HOST")
    if not token:
        raise ValueError("Переменная токена не задана")
    print(token)
    return TelegramBotConfig(token=token, port=port, host=host)