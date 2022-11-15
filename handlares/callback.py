from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


# @dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Какой национальный цветок Японии?"

    answers = [
        "Лотос",
        "Сакура",
        "Айгуль",
        "Гирень",
        "Гипсофилы",
        "Кактус",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Забей в гугле",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    question = "Что такое яой?"

    answers = [
        "напиток",
        "жанр японских комиксов",
        "марка детских подгузников",
        "модель телефона",
        "название мыломоющих средств",
        "название аниме"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Забей в гугле",
        open_period=10,
    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
