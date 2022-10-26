from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

#----- Main menu ----

btnRandom=KeyboardButton('Ссылка на дискорд совета')
btnOther=KeyboardButton('Другие вопросы')
btnOther1=KeyboardButton('Хочу отправить Жалобы/Предложения')
btnOther2=KeyboardButton('Редактировать свою анкету студента')
btnOther3=KeyboardButton('Ссылка на канал студ совета')
mainMenu=ReplyKeyboardMarkup(resize_keyboard = None,row_width=2).add(btnRandom,btnOther1,btnOther2,btnOther3,btnOther)

#----- Main menu ----
btnInfo=KeyboardButton('Хочу стать членом студ совета')
btnInfo1=KeyboardButton('Вопрос для устройства в IT')
btnInfo2=KeyboardButton('Вопрос по учебному процессу')
otherMenu=ReplyKeyboardMarkup(resize_keyboard = None,row_width=2).add(btnInfo,btnInfo1,btnInfo2,btnMain)