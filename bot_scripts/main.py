import telebot
from telebot import types
from data_base_scripts import DB

# @englik_bot

data_base = DB()

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


@bot.callback_query_handler(func = lambda call: True)
def buttons(call):
	call_data = call.data

	if call_data == 'signin':
		msg = bot.send_message(call.message.chat.id,'Введите логин:')
		bot.register_next_step_handler(msg, signin_login)

def signin_login(message):
	login = message.text
	res = data_base.get_user_data(login)
	if res != None:
		msg = bot.send_message(message.chat.id, '👍 Отлично! Введите пароль:')
		bot.register_next_step_handler(msg, signin_password)
	else:
		msg = bot.send_message(message.chat.id, 'К сожалению, учётной записи с таким логином не существует 😢\nВведите пароль для новой учётной записи с этим логином:')

# def signin_password(message):


bot.infinity_polling()