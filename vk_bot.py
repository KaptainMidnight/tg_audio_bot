import telebot
from vkbottle import Bot, Message
from vkbottle.rule import AttachmentRule
from database import Users

bot = Bot(tokens=['a698725881e84f995088a628c7c87a841c5282293e2ea647d442e1cb8b19ec72e09264d8705dd4820275f'])
telegram = telebot.TeleBot(token='1229780153:AAH4l5C9rVWNsLriS-sZpsEZlkQ3ek6Vfpg')


@bot.on.message(text='<telegram_id:int>')
async def wrapper(answer: Message, telegram_id):
    data = [(i.vk_id, i.telegram_id) for i in Users.select() if i.vk_id == answer.from_id]

    if not data:
        Users.create(vk_id=answer.from_id, telegram_id=telegram_id)
        await answer('Отправь мне аудиозаписи во вложении')
    else:
        await answer('Отправь мне аудиозаписи во вложении')


@bot.on.message(AttachmentRule('audio'))
async def wrapper(answer: Message):
    for attachment in answer.attachments:
        telegram_id = Users.get(Users.vk_id == str(answer.from_id)).telegram_id
        telegram.send_audio(chat_id=telegram_id,
                            audio=attachment.audio.url,
                            caption=f"{attachment.audio.artist} - {attachment.audio.title}")

    await answer('Мы отправили Вам аудиозаписи в Telegram')


bot.run_polling()
