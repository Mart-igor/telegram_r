from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from aiogram.fsm.context import FSMContext

import app.keybords as kb
from app.states import Register

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Yo', reply_markup=kb.main) # kogda bot otpravliet Yo srazy otpravit eshe klaviatyry
    await message.reply('hi')

@router.message(Command('help'))
async def help(message: Message):
    await message.answer('help')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выбирете категорию товара', reply_markup=kb.catalog)

@router.callback_query(F.data == 'G')
async def gg(callback: CallbackQuery):
    await callback.answer('Вы выбрали Г')
    await callback.message.answer('Вы выбрали G')



@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваши имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Введите номер', reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.contact)
    data = await state.get_data()
    await message.answer(f'Name: {data['name']}, age: {data['age']}\n phone: {data['number']}')
    await state.clear()