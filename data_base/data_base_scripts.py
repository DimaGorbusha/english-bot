import psycopg2


class DB:
    def __DB_connect(self) -> None: # Метод соединения с бд
        self.connection = psycopg2.connect(dbname='database', 
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
                    level INTEGER, 
                    name TEXT, 
                    score INTEGER)"""

                cursor.execute(sql_create_tb_test_data_query)
                
                sql_create_tb_test_descr_query = """CREATE TABLE IF NOT EXISTS free_tests (
                    test_id BIGSERIAL PRIMARY KEY,
                    question TEXT, 
                    answer TEXT, 
                    level TEXT)"""
                cursor.execute(sql_create_tb_test_descr_query)
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
                sql_update_users_level_query = """UPDATE users SET level = %s WHERE login = %s"""
                cursor.execute(sql_update_users_level_query, (level, login))
        finally:
            self.connection.close()

    
    def update_user_name(self, new_name: str, login: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = """UPDATE users SET name = %s WHERE login = %s"""
                cursor.execute(sql_update_user_name_query, (new_name, login))
        finally:

            self.connection.close()

    
    def update_user_score(self, score: int, login: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = """UPDATE users SET score = %s WHERE login = %s"""
                cursor.execute(sql_update_user_name_query, (score, login))
        finally:

            self.connection.close()


    def update_user_password(self, new_password: str, login: str) -> None: # Метод обновления пароля в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_user_name_query = """UPDATE users SET password = %s WHERE login = %s"""
                cursor.execute(sql_update_user_name_query, (new_password, login))
        finally:

            self.connection.close()

    
    def insert_description(self):
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True

        finally:
            self.connection.close()
