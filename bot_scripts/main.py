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
keyboard_login_menu = types.InlineKeyboardMarkup(row_width = 1)
keyboard_main_menu = types.InlineKeyboardMarkup(row_width = 2)

#----Кнопки----
login_menu_btn_signin = types.InlineKeyboardButton('🚪 Войти', callback_data = 'signin')
login_menu_btn_signup = types.InlineKeyboardButton('🔐 Зарегистрироваться', callback_data = 'signup')
main_menu_btn_start = types.InlineKeyboardButton('👩‍🏫 Начать учиться', callback_data='start_learn')
main_menu_btn_lessons = types.InlineKeyboardButton('🏫 Перейти к урокам', callback_data='lessons')
main_menu_btn_buy_lessons = types.InlineKeyboardButton('💵 Купить премиум-уроки', callback_data='buy_premium_lessons')
main_menu_btn_subscribe = types.InlineKeyboardButton('Купить подписку', callback_data='subscribe')

#----Добавление кнопок в клавы----
keyboard_login_menu.add(login_menu_btn_signin, login_menu_btn_signup) 
keyboard_main_menu.add(main_menu_btn_start, main_menu_btn_lessons, main_menu_btn_buy_lessons, main_menu_btn_subscribe)


#----Основной код----
@bot.message_handler(commands=['start'])
def start(message) -> None:	
	bot.send_message(message.chat.id, f'👋 Привет, я бот изучения английского языка для работников IT!\n Для начала, вам надо зарегистрироваться или войти:', reply_markup = keyboard_login_menu)


@bot.callback_query_handler(func = lambda call: True)
def buttons(call) -> None:
	call_data = call.data

	if call_data == 'signin':
		msg = bot.send_message(call.message.chat.id,'Введите логин:')
		bot.register_next_step_handler(msg, signin_login)

	elif call_data == 'signup':
		msg = bot.send_message(call.message.chat.id,'Введите логин для регистрации:')
		bot.register_next_step_handler(msg, signup_login)

def signin_login(message) -> None:
	login = message.text
	res = data_base.get_user_data(login)
	if res != None:
		msg = bot.send_message(message.chat.id, '👍 Отлично! Введите пароль:')
		signin_password(msg, login, res[0])
	else:
		msg = bot.send_message(message.chat.id, 'К сожалению, учётной записи с таким логином не существует 😢\nВведите пароль для новой учётной записи с этим логином:')

def signin_password(message, password:str) -> None:
	password_input = message.text
	if password_input == password:
		bot.send_message(message.chat.id, '')
		# ПРОПИСАТЬ ВХОД ПО ПАРОЛЮ
		# PASTE DB QUERY
	else:
		bot.send_message(message.chat.id, '😢 Неправильный пароль')
		signin_password(message, password)

def signup_login(message) -> None:
	login = message.text
	res = data_base.get_user_data(login)
	if res != None:
		msg = bot.send_message(message.chat.id, 'Учётная запись с таким логином уже существует. \nВведите пароль для входа:')
		signin_password(msg, login, res[0])
		# PASTE DB QUERY
	else:
		msg = bot.send_message(message.chat.id, '👍 Отлично! Теперь введите пароль:')
		signup_password(msg, login)


def signup_password(message, login: str) -> None:
	password_input = message.text
	# PASTE DB QUERY


def main_menu(message) -> None:
	bot.send_message(message.chat.id, 'Поздравляю, вы в главном меню! \nЧто вы хотите сделать?', reply_markup = keyboard_main_menu)


def entrance_test(message) -> None:
	bot.send_message(message.chat.id, 'Сейчас вам нужно пройти тест, чтобы я понял, какой у вас уровень английского языка.\nУдачи!')


def free_lesson():
	pass


bot.infinity_polling()