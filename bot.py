import aiogram
from aiogram import Bot, Dispatcher, executor ,types
import markup as nav


TOKEN = ""

bot = Bot(token=TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,'Привет студент {0.first_name}, тебя приветствует Jenkis, я представитель студ совета, тут ты сможешь задать свои вопросы или сделать парочку запросов'.format(message.from_user),reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_messahe(message: types.Message):
    if message.text=='Ссылка на дискорд совета':
        await bot.send_message(message.from_user.id,'https://discord.gg/9tFXtB9U')
    elif message.text == 'Хочу отправить Жалобы/Предложения':
        await bot.send_message(message.from_user.id, 'https://forms.gle/kkisZKcpJMxF3ZKXA')
    elif message.text == 'Ссылка на канал студ совета':
        await bot.send_message(message.from_user.id, 'https://t.me/+tIBw0XpWaUxjMDMy')
    elif message.text == 'Редактировать свою анкету студента':
        await bot.send_message(message.from_user.id, 'https://forms.gle/Fr2K1b31bNUCHNa49')
    elif message.text=='Главное меню':
        await bot.send_message(message.from_user.id,'Главное меню',reply_markup=nav.mainMenu)
    elif message.text=='Другие вопросы':
        await bot.send_message(message.from_user.id,'Другие вопросы',reply_markup=nav.otherMenu)
    elif message.text=='Хочу стать членом студ совета':
        await bot.send_message(message.from_user.id,'https://t.me/Che_shi4')
    elif message.text=='Вопрос для устройства в IT':
        await bot.send_message(message.from_user.id,'https://t.me/Che_shi4')
    elif message.text == 'Вопрос по учебному процессу':
        await bot.send_message(message.from_user.id, 'https://t.me/Che_shi4')
    else:
        await message.reply('Неизвестаня команда')

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)