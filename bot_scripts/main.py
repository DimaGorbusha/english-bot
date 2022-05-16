import telebot
from telebot import types

# @englik_bot

config = {
	'token': '5394720791:AAH7s71_8P3rnOqSvVh4b5de6TOtokHFqV4'
}

bot = telebot.TeleBot(config['token'])

#----Клавиатуры----
keyboard_main_menu = types.InlineKeyboardMarkup(row_width = 1)
main_menu_btn_signin = types.InlineKeyboardButton('🚪 Войти', callback_data = 'signin')
main_menu_btn_signup = types.InlineKeyboardButton('🔐 Зарегистрироваться', callback_data = 'signup')
keyboard_main_menu.add(main_menu_btn_signin, main_menu_btn_signup) 

@bot.message_handler(commands=['start'])
def start(message):	
	bot.send_message(message.chat.id, f'👋 Привет, я бот для изучения английского языка!\n Для начала, вам надо зарегистрироваться или войти:', reply_markup = keyboard_main_menu) 

bot.infinity_polling()