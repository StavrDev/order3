from aiogram import executor, Bot, Dispatcher, types
from pyrogram import Client
import time

class TgBot:
    def __init__(
                        self,
                        token,
                        keyboard_start, 
                        kb_set_time, api_id, api_hash
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
                await message.answer('Выберите время отправки', reply_markup=kb_set_time)

            async def keyboard(callback: types.CallbackQuery):
                btn_data = callback.data
                chat_id = callback.message.chat.id
                
                if btn_data == "text":
                    await self.bot.send_message(chat_id, 'Введите текст')
            
                if btn_data == "set_time":
                    await self.bot.send_message(chat_id, 'Выберите время отправки', reply_markup=kb_set_time)

                if btn_data == "5time":
                    await self.bot.send_message(chat_id, 'Собщение будет отправляться каждые 5 минут')
                    while 1:
                        time.sleep(3)

                        app = Client("my_account", api_id, api_hash)
                        await app.start()
                        f = open('text.txt', 'r')
                        text = f.read()
                        await app.send_message(chat_id=-1001875453883, text = text)
                        await app.stop()


            self.dp.register_message_handler(start_command, commands=["start"])
            self.dp.register_callback_query_handler(keyboard)
            self.dp.register_message_handler(set_text)

    def start(self):
        executor.start_polling(
                                    self.dp,
                                    skip_updates=True
                                    )       