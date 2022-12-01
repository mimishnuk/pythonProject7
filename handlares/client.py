from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from keybords.clients_keybords import start_markup
from parser import animee

# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Охаёёё {message.from_user.first_name}",
                           reply_markup=start_markup)


async def info_handler(message: types.Message):
    await message.reply("Посмотри в справочнике")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько полос на флаге США?"
    answers = [
        "56",
        '21',
        '13',
        '11',
        '9',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="иди учиться",
        open_period=10,
        reply_markup=markup
    )


# @dp.message_handler(commands=['mem'])
async def mem_1(message: types.Message):
    photo = open("media/5.jpeg", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def pin(message: types.Message):
    if message.reply_to_message:
        await  bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, f"ответь")


async def parser_anime(message: types.Message):
    items = animee.parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"{item['status']}\n"
            f"#Y{item['year']}\n"
            f"#{item['country']}\n"
            f"#{item['genre']}\n"
        )

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_1, commands=['mem'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(pin, commands=["pin"], commands_prefix='!')
    dp.register_message_handler(parser_anime, commands=["anime"])


