import random
from aiogram import Dispatcher, types
from config import bot, ADMIN

async def game(message: types.Message):
    if message.from_user.id in ADMIN:
        emojies = ['⚽', '🏀', '🎰', '🎲', '🎯', '🎳']
        emoji = random.choice(emojies)
        await bot.send_dice(message.chat.id, emoji=emoji)
    else:
        await message.answer("ты не мой босс!")

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['emoji'])