from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor #для запуска бота
import logging
import decouple
from decouple import config

# decouple для того что-бы скрывать определенную инфу
# logging для выведения расширенной информации
# Bot это токен бота
# Dispatcher это перехватчик смс
# types свои типы данных в aiogram


TOKEN=config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

@db.message_handler(commands=['start' , 'hello'])
async def start_handler(massage:types.message):
    await bot.send_message(massage.from_user.id,f'{massage.from_user.first_name}')
    await massage.answer('Привет, это бот!')
    # await massage.reply(massage.from_user.first_name)



@db.message_handler()
async def echo(massege:types.Message):
    await bot.send_message(massege.from_user.id,massege.text)
    await massege.answer('На этом всё!')




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
