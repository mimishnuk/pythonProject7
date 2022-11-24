# FSM- Finite State Machine
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keybords.clients_keybords import submit_markup, cancel_markup
from database.bot_db import sqlite_command_insert

class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer("Привет ментор, ай свой id",
                             reply_markup=cancel_markup)
    else:
        await message.answer("напишите в личку")


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] =f'@{message.from_user.username}'
    await FSMAdmin.next()
    await message.answer("введите имя")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("направление?")

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("ваш возраст?")


async def load_age(message: types.Message, state: FSMContext):
    try:
        if 15 < int(message.text) < 60:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Какая группа?")
        else:
            await message.answer("Доступ воспрещен!")
    except:
        await message.answer("Пиши нормально!")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMAdmin.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)
    await bot.send_message(message.chat.id, f"имя - {data['name']}\n"
                                            f"направление - {data['direction']}\n"
                                            f"возраст - {data['age']}\n"
                                            f"группа - {data['group']}")

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sqlite_command_insert(state)
        await state.finish()
        await message.answer("Все свободен!")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer("запрос неверный")

        


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена")


def registor_handler_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands={'reg'})
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)