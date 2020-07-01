import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot.types import Message

bot = telebot.TeleBot('1229780153:AAH4l5C9rVWNsLriS-sZpsEZlkQ3ek6Vfpg')


@bot.message_handler(commands=['start'])
def welcome_handler(message: Message):
    keyboard = InlineKeyboardMarkup()
    confirm = InlineKeyboardButton(
        text='Перейти в группу',
        url='https://vk.com/im?sel=-195781697'
    )
    keyboard.add(confirm)
    bot.send_message(message.chat.id,
                     text=f'Пришли в нашу группу код: *{message.chat.id}*',
                     reply_markup=keyboard,
                     disable_web_page_preview=True,
                     parse_mode='markdown')


bot.polling(none_stop=True)
