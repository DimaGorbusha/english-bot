import psycopg2
from random import randint
# huy\\//govno228
class DB:
    """
        Класс базы данных со всеми методами для получения, изменения всех данных в таблицах.
        Существует три таблицы: users - таблица с пользователями и их данными (логин, пароль, уровень знания англа, имя для обращения в боте, количество очков), одна строка - один пользователь; free_tests - бесплатные вопросы и ответы (уровень, вопрос, ответ), одна строка - один вопрос/ответ; premium_tests - платные вопросы и ответы (уровень, вопрос, ответ), одна строка - один вопрос/ответ.
    """
    def __DB_connect(self) -> None: # Метод соединения с бд
        self.connection = psycopg2.connect(dbname='postgres', 
                                    user='postgres', 
                                    password='$NS$//1907',
                                    host='localhost')


    def __init__(self) -> None: # Метод инициализации объекта классаа
        self.__create_table()

    def __create_table(self) -> None: # Метод создания таблиц
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_create_tb_test_data_query = """CREATE TABLE IF NOT EXISTS users (
                    chat_id TEXT PRIMARY KEY,
                    login TEXT UNIQUE, 
                    password TEXT, 
                    name TEXT, 
                    score INTEGER,
                    sub_multiplier INTEGER)""" # Создание таблицы пользователей
                cursor.execute(sql_create_tb_test_data_query)
                
                sql_create_tb_free_test_query = """CREATE TABLE IF NOT EXISTS free_tests (
                    test_id BIGSERIAL PRIMARY KEY,
                    question TEXT, 
                    answer TEXT)""" # Создание таблицы бесплатных тестов
                cursor.execute(sql_create_tb_free_test_query)

                sql_create_tb_premium_test_query = """CREATE TABLE IF NOT EXISTS premium_tests (
                    test_id BIGSERIAL PRIMARY KEY,
                    link TEXT,
                    answer TEXT)""" # Создание таблицы платных тестов с голосовыми
                cursor.execute(sql_create_tb_premium_test_query)
        finally:
            self.connection.close()


    def insert_data_user(self, login: str, chat_id: str, password: str, name: str, score: int, sub_multiplier: int) -> None: # Метод создания новой записи в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO users (chat_id, login, password, name, score, sub_multiplier) VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                             chat_id, login, password, name, score, sub_multiplier))
        finally:
            self.connection.close()

    
    def update_user_name(self, new_name: str, chat_id: str) -> None: # Метод обновления имени
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = """UPDATE users SET name = %s WHERE login = %s"""
                cursor.execute(sql_update_user_name_query, (new_name, chat_id))
        finally:

            self.connection.close()

    
    def update_user_score(self, score: int, chat_id: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = """UPDATE users SET score = %s WHERE login = %s"""
                cursor.execute(sql_update_user_name_query, (score, chat_id))
        finally: 

            self.connection.close()


    def update_user_password(self, new_password: str, chat_id: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = """UPDATE users SET password = %s WHERE chat_id = %s"""
                cursor.execute(sql_update_user_name_query, (new_password, chat_id))
        finally:

            self.connection.close()

    
    def get_user_data(self, chat_id:str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT chat_id, login, password, name, score  FROM users WHERE chat_id = %s"""
                cursor.execute(sql_find_login_query, (chat_id,))
                return list(cursor.fetchone())
        finally:
            self.connection.close()


    def get_free_test_data(self) -> list: # Получение вопроса и ответа бесплатного теста
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_get_test_data_query = """SELECT question, answer  FROM free_tests WHERE test_id = %s"""
                cursor.execute(sql_get_test_data_query, (randint(0, 5),))
                return list(self.cursor.fetchone())

        finally:
            self.connection.close()

    
    def get_premium_test_data(self):
        pass
    # INPUT SENDING AUDIO FROM LINKS


    def increase_user_score(self, chat_id:str) -> None: # Метод увеличения кол-ва очков юзвера по логину
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                user_data  = self.get_user_data(chat_id)
                user_data[5] += 100
                sql_update_user_score_query = """UPDATE users SET score = %s WHERE chat_id = %s """
                cursor.execute(sql_update_user_score_query, (user_data[5], chat_id))

        finally:
            self.connection.close()