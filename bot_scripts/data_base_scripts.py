import psycopg2
from random import randint

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
        self.__DB_connect()
        self.connection.close()

    def create_table(self) -> None: # Метод создания таблиц
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_create_tb_test_data_query = """CREATE TABLE IF NOT EXISTS users (
                    login TEXT PRIMARY KEY, 
                    password TEXT,
                    level TEXT, 
                    name TEXT, 
                    score INTEGER)""" # Создание таблицы пользователей
                cursor.execute(sql_create_tb_test_data_query)
                
                sql_create_tb_free_test_query = """CREATE TABLE IF NOT EXISTS free_tests (
                    test_id BIGSERIAL PRIMARY KEY,
                    question TEXT, 
                    answer TEXT, 
                    level TEXT)""" # Создание таблицы бесплатных тестов
                cursor.execute(sql_create_tb_free_test_query)

                sql_create_tb_premium_test_query = """CREATE TABLE IF NOT EXISTS premium_tests (
                    test_id BIGSERIAL PRIMARY KEY,
                    link TEXT, 
                    answer TEXT, 
                    level TEXT)""" # Создание таблицы платных тестов с голосовыми
                cursor.execute(sql_create_tb_premium_test_query)
        finally:
            self.connection.close()


    def insert_data_users(self, login: str, password: str, level: int, name: str, score: int) -> None: # Метод создания новой записи в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO users (login, password,
                level, name, score) VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                            login, password, level, name, score))
        finally:
            self.connection.close()

    
    def __find_login(self, login: str) -> bool: # Метод поиска логина пользователя из бд
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = f"SELECT login FROM users WHERE login = {login}"
                cursor.execute(sql_find_login_query)
                res = self.cursor.fetchone()
                return res != None
        finally:
            self.connection.close()


    def update_user_level(self, login: str, level: int) -> None: # Метод обновления уровня знания английского в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_users_level_query = f"UPDATE users SET level = {level} WHERE login = {login}"
                cursor.execute(sql_update_users_level_query)
        finally:
            self.connection.close()

    
    def update_user_name(self, new_name: str, login: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = f"UPDATE users SET name = {new_name} WHERE login = {login}"
                cursor.execute(sql_update_user_name_query)
        finally:

            self.connection.close()

    
    def update_user_score(self, score: int, login: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = f"UPDATE users SET score = {score} WHERE login = {login}"
                cursor.execute(sql_update_user_name_query)
        finally:

            self.connection.close()


    def update_user_password(self, new_password: str, login: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = f"UPDATE users SET password = {new_password} WHERE login = {login}"
                cursor.execute(sql_update_user_name_query)
        finally:

            self.connection.close()

    
    def get_user_data(self, login:str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = f"SELECT password, level, name, score  FROM users WHERE login = {login}"
                cursor.execute(sql_find_login_query)
                return list(self.cursor.fetchone())
        finally:
            self.connection.close()


    def insert_description(self):
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True

        finally:
            self.connection.close()


    def get_test_data(self) -> list:
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                num_test = randint(0, 120)
                sql_get_test_data_query = f"SELECT question, answer  FROM free_tests WHERE test_id = {num_test}"
                cursor.execute(sql_get_test_data_query)
                return list(self.cursor.fetchone())

        finally:
            self.connection.close()


    def get_free_test_data(self, login:str) -> list: # Получение вопроса и ответа бесплатного теста
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                level  = self.get_user_data(login)
                level = level[1]
                sql_get_test_data_query = f"SELECT question, answer  FROM free_tests WHERE level = {level}"
                cursor.execute(sql_get_test_data_query)
                return list(self.cursor.fetchone())

        finally:
            self.connection.close()


    def increase_user_score(self, login:str) -> None: # Метод увеличения кол-ва очков юзвера по логину
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                user_data  = self.get_user_data(login)
                user_data[3] += 100
                sql_update_user_score_query = f"UPDATE users SET score = {user_data[3]} WHERE login = {login}"
                cursor.execute(sql_update_user_score_query)

        finally:
            self.connection.close()
