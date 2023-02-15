from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# inline для кнопок
# decouple длятого чтобы скрывать определенную инфу
# logging для выведения расширенной информации

# Bot это токен бота
# Dispatcher это перехватчик смс
# types свои типы данных в aiogram


TOKEN = config('TOKEN')
# TOKEN = '6117087222:AAHIS7VCbbcn_6m1aVK1HMwc_EN7TpxTe-M'

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)


@db.message_handler(commands=['start', 'hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}')
    await massage.answer('это ансфер')
    await massage.reply(massage.from_user.first_name)


# опросник\викторина
@db.message_handler(commands=['quiz'])
async def quiz1(massage: types.Message):
    # создание кнопок
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    # привязать кнопки к опроснику
    # создание опросника

    ques = 'кто ты воин?'
    answer = [
        'Бетмен-рыцарь ночи',
        'томас шелби из семьи острые козырьки',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'диктор канала "Мастерская настроения"',
        'оптимус прайм последний прайм'
    ]
    # await massage.answer_poll()
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='ты ахилесс',
        open_period=15,
        reply_markup=markup
    )


@db.callback_query_handler(text='button')
# перехватчик нажатия кнопки
async def quiz2(call: types.CallbackQuery):
    ques = 'что это?'
    answer = [
        'Бетмен-рыцарь ночи',
        'томас шелби из семьи острые козырьки',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'диктор канала "Мастерская настроения"',
        'оптимус прайм последний прайм'
    ]
    photo = open('media/cambg_6.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='это бетмен ты угадал',
        open_period=15,

    )


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)