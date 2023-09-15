from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn1 = InlineKeyboardButton("Настроить рассылку", callback_data='text')
btn2 = InlineKeyboardButton("Запустить", callback_data='start')
kb_start = InlineKeyboardMarkup(row_width=2).add(btn1, btn2)


kb_m = InlineKeyboardMarkup(row_width=3)
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
for month in months:
    kb_m.add(InlineKeyboardButton(text=month, callback_data=month))

timezones = [
    "UTC−5",
    "UTC-6",
    "UTC-7",
    "UTC-8"
]
kb_set_time = InlineKeyboardMarkup(row_width=2)
    
for tz in timezones:
    btn = InlineKeyboardButton(text=tz, callback_data=tz)
    kb_set_time.insert(btn)

kb_days = InlineKeyboardMarkup(row_width=10)
for day in range(1, 31):
        button = InlineKeyboardButton(str(day), callback_data=str(day))
        kb_days.add(button)

kb_time = InlineKeyboardMarkup(row_width=1)
times = ['10:00-13:00', "14:00-17:00", "18:00-21:00"]
for time in times:
     kb_time.add(InlineKeyboardButton(time, callback_data=time))

btn1 = InlineKeyboardButton("Ввести текст", callback_data='text')
kb_data = InlineKeyboardMarkup(row_width=2).add(btn1, btn2)