from aiogram import executor, Bot, Dispatcher, types
from pyrogram import Client
from datetime import datetime
import pytz
import time
import os
import asyncio

class TgBot:
    def __init__(
                        self,
                        token,
                        keyboard_start, 
                        kb_set_time,
                          api_id, 
                          api_hash, 
                          kb_m, 
                          kb_time, 
                          kb_days,
                          chat_id_channel
                    ):
                    
            
            self.bot = Bot(token=token)
            self.dp = Dispatcher(self.bot)

            async def start_command(message: types.Message):
                await message.answer("Вы попали в бота для рекламы.\n\nДля продолжения выберите действие:", reply_markup=keyboard_start)
            
            async def set_text(message:types.Message):
                text = message.text
                f = open ("text.txt", 'w')
                f.write(text)
                f.close()
                await message.answer('Добавьте файл(txt формат)')

            async def keyboard(callback: types.CallbackQuery):
                btn_data = callback.data
                message_id = callback.message.message_id
                global chat_id
                chat_id = callback.message.chat.id
                
                if btn_data == "text":
                    await self.bot.edit_message_text(chat_id = chat_id, text='Введите текст',message_id=message_id)
                    
                if btn_data  == 'Январь':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("01.")
                    f.close()
                if btn_data  == 'Февраль':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("02.")
                    f.close()
                if btn_data  == 'Апрель':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("04.")
                    f.close()
                if btn_data  == 'Май':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("05.")
                    f.close()
                if btn_data  == 'Июнь':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("06.")
                    f.close()
                if btn_data  == 'Июль':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("07.")
                    f.close()
                if btn_data  == 'Август':
                    await self.bot.edit_message_text(chat_id = chat_id, text= "Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("08.")
                    f.close()
                if btn_data  == 'Сентябрь':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("09.")
                    f.close()
                if btn_data  == 'Октябрь':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("10.")
                    f.close()
                if btn_data  == 'Ноябрь':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("11.")
                    f.close()
                if btn_data  == 'Декабрь':
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите день", reply_markup=kb_days, message_id=message_id)
                    f = open ('date.txt', 'a')
                    f.write("12.")
                    f.close()

                if btn_data == "1":
                    await self.bot.edit_message_text(chat_idchat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)

                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "2":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "3":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "4":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "5":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "6":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "7":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "8":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "9":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "10":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "11":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "12":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "13":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "14":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "15":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "16":
                    await self.bot.edit_message_text(chat_id = chat_id, text= "Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "17":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "18":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "19":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "20":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "21":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "22":
                    await self.bot.edit_message_text(chat_id = chat_id, text= "Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "23":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "24":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "25":
                    await self.bot.edit_message_text(chat_id = chat_id, text= "Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "26":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "27":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "28":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "29":
                    await self.bot.edit_message_text(chat_id = chat_id, text= "Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "30":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите часовой пояс", reply_markup=kb_set_time, message_id=message_id)
                    
                    f = open ('date.txt', 'a')
                    f.write("01.2023")
                    f.close()

                if btn_data == "UTC-5": 

                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите время отправки", reply_markup=kb_time, message_id=message_id)
                    f = open ("timezone.txt", 'a')
                    f.write('America/New_York')
                    f.close()

                if btn_data == "UTC-6":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите время отправки", reply_markup=kb_time, message_id=message_id)

                    f = open ("timezone.txt", 'a')
                    f.write('America/Chicago')
                    f.close()

                if btn_data == "UTC-7":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите время отправки", reply_markup=kb_time, message_id=message_id)

                    f = open ("timezone.txt", 'a')
                    f.write('America/Denver')
                    f.close()

                if btn_data == "UTC-8":
                    await self.bot.edit_message_text(chat_id = chat_id, text="Выберите время отправки", reply_markup=kb_time, message_id=message_id)

                    f = open ("timezone.txt", 'a')
                    f.write('America/Los_Angeles')
                    f.close()

                if btn_data == "10:00-13:00":
                    await self.bot.edit_message_text(chat_id = chat_id, text='Сохранено', reply_markup=keyboard_start, message_id=message_id)
                    
                    f = open ("time.txt", 'a')
                    f.write("11:00")
                    f.close()
                
                if btn_data == "14:00-17:00":

                    await self.bot.edit_message_text(chat_id = chat_id, text='Сохранено', reply_markup=keyboard_start, message_id=message_id)
                    
                    f = open ("time.txt", 'a')
                    f.write("15:00")
                    f.close()

                if btn_data == "18:00-21:00":

                    await self.bot.edit_message_text(chat_id = chat_id, text='Сохранено', reply_markup=keyboard_start, message_id=message_id)
                    
                    f = open ("time.txt", 'a')
                    f.write("19:00")
                    f.close()

                if btn_data == "start":
                    await self.bot.edit_message_text("Рассылка запущена", chat_id = chat_id, message_id=message_id)
                    try:
                        f = open('date.txt', 'r')
                        data = f.read()
                        f_t = open('time.txt', 'r')
                        time = f_t.read()
                            
                        date = datetime.strptime(data, '%m.%d.%Y')
                        time = datetime.strptime(time, '%H:%M').time()
                        tz = open('timezone.txt','r')
                        timezon = tz.read()
                        
                        scheduled_datetime = datetime.combine(date, time)
                        
                        timezone = pytz.timezone(timezon)
                        scheduled_datetime = timezone.localize(scheduled_datetime)

                        f.close()
                        f_t.close()
                        tz.close()
                        # Get the current datetime in UTC timezone
                        now = datetime.now(pytz.utc)

                        os.remove('date.txt') 
                        os.remove('time.txt') 
                        os.remove('timezone.txt') 

                        if scheduled_datetime > now:
                                # Calculate the delay until the scheduled datetime
                            delay = (scheduled_datetime - now).total_seconds()
                                
                                # Wait for the specified delay
                            asyncio.sleep(delay)
                                
                                # Send the scheduled message to the user
                            app = Client("my_account", api_id, api_hash)
                            await app.start()
                            
                            f = open('text.txt', 'r')
                            text = f.read()
                            file_path = "file.txt"


                            await app.send_document(chat_id=chat_id_channel, document=file_path, caption=text)
                            
                            await app.stop()
                        else:
                            await self.bot.send_message(chat_id, "Ненастоящая дата", reply_markup=keyboard_start)
                            os.remove('date.txt') 
                            os.remove('time.txt') 
                            os.remove('timezone.txt') 
                    except (ValueError, IndexError):
                            await self.bot.send_message(chat_id, "Ошибка в заполнение, попробуйте перезаполнить", reply_markup=keyboard_start)
                            os.remove('date.txt') 
                            os.remove('time.txt') 
                            os.remove('timezone.txt') 
                                
                
            
            async def handle_file(message: types.Message):
                if message.document:
                    
                    file_id = message.document.file_id
                    file_info = await self.bot.get_file(file_id)
                    file_path = file_info.file_path

                    await self.bot.download_file(file_path, f'file.txt')
                    await message.answer("Выберите месяц отправки:", reply_markup=kb_m)




            self.dp.register_message_handler(start_command, commands=["start"]) 
            self.dp.register_callback_query_handler(keyboard)
            self.dp.register_message_handler(set_text)
            self.dp.register_message_handler(handle_file,   content_types=types.ContentTypes.DOCUMENT )

    def start(self):
        executor.start_polling(
                                    self.dp,
                                    skip_updates=True
                                    )       