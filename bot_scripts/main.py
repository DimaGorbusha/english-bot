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
keyboard_back = types.InlineKeyboardMarkup(row_width = 1)

#----Кнопки----
login_menu_btn_signin = types.InlineKeyboardButton('🚪 Войти', callback_data = 'signin')
login_menu_btn_signup = types.InlineKeyboardButton('🔐 Зарегистрироваться', callback_data = 'signup')
main_menu_btn_start = types.InlineKeyboardButton('👩‍🏫 Начать учиться', callback_data='start_learn')
main_menu_btn_lessons = types.InlineKeyboardButton('🏫 Перейти к урокам', callback_data='lessons')
main_menu_btn_buy_lessons = types.InlineKeyboardButton('💵 Купить премиум-уроки', callback_data='buy_premium_lessons')
main_menu_btn_subscribe = types.InlineKeyboardButton('💵 Купить подписку', callback_data='subscribe')
main_menu_btn_info = types.InlineKeyboardButton('ℹ️ FAQ', callback_data='info')
back_btn = types.InlineKeyboardButton('⬅️ Назад', callback_data='back')

#----Добавление кнопок в клавы----
keyboard_login_menu.add(login_menu_btn_signin, login_menu_btn_signup) 
keyboard_main_menu.add(main_menu_btn_start, main_menu_btn_lessons, main_menu_btn_buy_lessons, main_menu_btn_subscribe, main_menu_btn_info)
keyboard_back.add(back_btn)


#----Основной код----
@bot.message_handler(commands=['start']) # Обработчик команды старт
def start(message) -> None:	
	bot.send_message(message.chat.id, f'👋 Привет, я бот изучения английского языка для работников IT!\n Для начала, вам надо зарегистрироваться или войти:', reply_markup = keyboard_login_menu)


@bot.callback_query_handler(func = lambda call: True) # Обработчик callback'а
def callback_processing(call) -> None:
	call_data = call.data

	if call_data == 'signin': # Функция входа
		msg = bot.send_message(call.message.chat.id,'Введите электронную почту:')
		bot.register_next_step_handler(msg, signin_login)

	elif call_data == 'signup': # Функция регистрации
		msg = bot.send_message(call.message.chat.id,'Введите электронную почту для регистрации:')
		bot.register_next_step_handler(msg, signup_login)

	elif call_data == 'info': # ПРОПИСАТЬ ИНФУ О БОТЕ: КАК ЮЗАТЬ И ТД
		msg = bot.send_message(call.message.chat.id, 'Введите логин для регистрации:', reply_markup = keyboard_back)

	elif call_data == 'back': # Возврат назад
		main_menu()


def signin_login(message) -> None: # Метод ввода логина для входа
	login = message.text
	res = data_base.get_user_data(login)
	if res != None:
		msg = bot.send_message(message.chat.id, '👍 Отлично! Введите пароль:')
		signin_password(msg, login, res[0])
	else:
		msg = bot.send_message(message.chat.id, 'К сожалению, учётной записи с такой электронной почтой не существует 😢\nВведите пароль для новой учётной записи с этой электронной почтой:')


def signin_password(message, password:str) -> None: # Метод ввода пароля для входа
	password_input = message.text
	if password_input == password:
		bot.send_message(message.chat.id, '')
		# ПРОПИСАТЬ ВХОД ПО ПАРОЛЮ
		# PASTE DB QUERY
	else:
		bot.send_message(message.chat.id, '😢 Неправильный пароль')
		signin_password(message, password)


def signup_login(message) -> None: # Метод ввода логина для регистрации
	login = message.text
	res = data_base.get_user_data(login)
	if res != None:
		msg = bot.send_message(message.chat.id, 'Учётная запись с таким логином уже существует. \nВведите пароль для входа:')
		signin_password(msg, login, res[0])
		# PASTE DB QUERY
	else:
		msg = bot.send_message(message.chat.id, '👍 Отлично! Теперь введите пароль:')
		signup_password(msg, login)


def signup_password(message, login: str) -> None: # Метод ввода пароля для регистрации
	password_input = message.text
	# PASTE DB QUERY


def main_menu(message = None) -> None:
	bot.send_message(message.chat.id, 'Поздравляю, вы в главном меню! \nЧто вы хотите сделать?', reply_markup = keyboard_main_menu)


def entrance_test(message) -> None:
	bot.send_message(message.chat.id, 'Сейчас вам нужно пройти тест, чтобы я понял, какой у вас уровень английского языка.\nУдачи!')
	test_data = data_base.get_entrance_test_data()
	bot.send_message(message.chat.id, test_data[0])
	answer = message.text
	if answer == test_data[1]:
		bot.send_message(message.chat.id, '👍  Правильно!')
		right_answer += 1
	else:
		bot.send_message(message.chat.id, '😢 Неправильно!')



def free_lesson(message):
	test_data = data_base.get_entrance_test_data()
	bot.send_message(message.chat.id, test_data[0])
	answer = message.text
	if answer == test_data[1]:
		bot.send_message(message.chat.id, '👍  Правильно!')
		data_base.increase_user_score()
	else:
		bot.send_message(message.chat.id, '😢 Неправильно!')


bot.infinity_polling()