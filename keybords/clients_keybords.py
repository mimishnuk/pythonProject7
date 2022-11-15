from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz')

start_markup.add(start_button, info_button)