import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('Ok!')


async def go_to_study():
    await bot.send_message(chat_id=chat_id, text="Иди на учебу!")


async def go_to_eat():
    await bot.send_message(chat_id=chat_id, text="Пожалуйста покушай")


async def scheduler():
    aioschedule.every().monday.at('06:30').do(go_to_study)
    aioschedule.every().thursday.at('21:20').do(go_to_eat)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)