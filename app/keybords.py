from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Карзина')],
    [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')


catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='galaxies', callback_data='G')],
                                                [InlineKeyboardButton(text='planets', callback_data='P')],
                                                [InlineKeyboardButton(text='starts', callback_data='S')],
                                                [InlineKeyboardButton(text='unknown', callback_data='Q')],
                                                ])


get_number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)]],
    resize_keyboard=True)

