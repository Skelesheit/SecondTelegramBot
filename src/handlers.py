from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from src.states import LangParseForm
from utils.lang_data import program_langs, lang_frameworks
from utils.models import FrameworkLink
from utils.parser import get_titles, get_info_from_title
from utils.functions import split_message

router: Router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.set_state(LangParseForm.lang)

    kb = [ KeyboardButton(text=lang) for lang in program_langs ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=[kb],
        resize_keyboard=True,
        input_field_placeholder="Выберите свой язык программирования"
    )

    await message.answer(f"Привет, {message.from_user.first_name}! Это бот по программированию.\n"
                         f"Какой язык программирования ты предпочитаешь?",
                         reply_markup=keyboard)

@router.message(LangParseForm.lang, F.text.in_(program_langs))
async def process_lang(message: Message, state: FSMContext) -> None:
    language = message.text
    frameworks: list[FrameworkLink] = lang_frameworks[language]
    fw_names:list[str] = [framework.framework for framework in frameworks]
    await state.update_data(language=language)
    await state.set_state(LangParseForm.framework)
    kb = [KeyboardButton(text=name) for name in fw_names]
    keyboard = ReplyKeyboardMarkup(
        keyboard=[kb],
        resize_keyboard=True,
        input_field_placeholder="Выберите свой фреймворк"
    )

    text = "\n".join(fw_names)
    await message.reply(f"Отличный выбор! А с каким фреймворком работаете? "
                        f"Выберите один из списка: \n"
                        f"{text}", reply_markup=keyboard)

@router.message(LangParseForm.lang)
async def lang_chosen_incorrectly(message: Message):
    kb = [KeyboardButton(text=lang) for lang in program_langs]
    keyboard = ReplyKeyboardMarkup(
        keyboard=[kb],
        resize_keyboard=True,
        input_field_placeholder="Выберите свой язык программирования"
    )
    await message.answer(
        text="Я не знаю такого язка.\n\n"
             "Пожалуйста, выберите один из языков ниже:",
        reply_markup=keyboard
    )

@router.message(LangParseForm.framework)
async def process_framework(message: Message, state: FSMContext) -> None:
    framework = message.text
    await state.update_data(framework=framework)
    await state.set_state(LangParseForm.title)
    data = await state.get_data()
    language = data.get('language')
    link_framework = ''
    for item in lang_frameworks[language]:
        if item.framework == framework:
            link_framework = item.link
    if not link_framework:
        await message.reply("Такого фреймворка я не знаю!")
    print(link_framework)
    titles = await get_titles(link_framework)
    title_links = { title.title: title.link for title in titles }
    await state.update_data(links=title_links)
    kb = [ KeyboardButton(text= title.title) for title in titles ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=[kb],
        resize_keyboard=True,
        input_field_placeholder="Выберите главу"
    )
    title_names: list[str] = [title.title for title in titles]
    text = "\n".join(title_names)

    await message.reply(f"хорошо, теперь выберите главу, с которой хотите ознакомиться: \n"
                        f"{text}", reply_markup=keyboard)


@router.message(LangParseForm.title)
async def give_final_parse(message: Message, state: FSMContext) -> None:
    await state.update_data(title=message.text)
    data = await state.get_data()
    links = data.get('links')
    current_link =  links[message.text]
    print(current_link)
    text = await get_info_from_title(current_link)
    text_parts = split_message(text)
    await state.clear()
    await message.reply(f"Вот что я нашёл: ")
    for part in text_parts:
        await message.reply(part)


@router.message(Command("/restart"))
async def cmd_restart(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    print("restart")
    if current_state is None:
        return
    await state.clear()
    await message.answer(
        "restart.",
        reply_markup=ReplyKeyboardRemove(),
    )
