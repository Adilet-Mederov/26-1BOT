from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor #для запуска бота
import logging
import decouple
from decouple import config

TOKEN=config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

@db.message_handler(commands=['start' , 'hello'])
async def start_handler(massage:types.message):
    await massage.answer('HELLO!')
    await bot.send_message(massage.from_user.id,f'{massage.from_user.first_name}')
    await massage.answer('Пока что всё!')

@db.message_handler()
async def echo(massege:types.Message):
    await bot.send_message(massege.from_user.id,massege.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)



