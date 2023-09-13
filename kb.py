from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn1 = InlineKeyboardButton("Ввести текст рекламы", callback_data='text')
btn2 = InlineKeyboardButton("Выбрать время рассылки", callback_data='set_time')
kb_start = InlineKeyboardMarkup(row_width=2).add(btn1, btn2)

btn1 = InlineKeyboardButton('Каждые 5 минут', callback_data='5time')
btn2 = InlineKeyboardButton('Каждые 10 минут', callback_data='10time')
btn3 = InlineKeyboardButton('Каждые 30 минут', callback_data='30time')
btn4 = InlineKeyboardButton('Каждый час', callback_data='60time')
btn5 = InlineKeyboardButton('Каждые 3 часа', callback_data='180time')
kb_set_time = InlineKeyboardMarkup(row_width=2).add(btn1, btn2, btn3, btn4, btn5)