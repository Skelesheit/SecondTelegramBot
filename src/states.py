from aiogram.fsm.state import StatesGroup, State


class LangParseForm(StatesGroup):
    lang = State()
    framework = State()
    title = State()
    links = State()