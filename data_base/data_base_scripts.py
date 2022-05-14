import psycopg2


class DB:
    def DB_connect(self) -> None:
        self.connection = psycopg2.connect(dbname='database', 
                                    user='postgres', 
                                    password='$NS$//1907',
                                    host='localhost')


    def __init__(self) -> None:
        self.DB_connect()
        self.connection.close()

    def create_table(self) -> None:
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_create_tb_test_data_query = """CREATE TABLE IF NOT EXISTS users (
                    login TEXT PRIMARY KEY, 
                    password TEXT,
                    level TEXT, 
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

    def insert_descriptin(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True

        finally:
            self.connection.close()

    def insert_data_users(self, login: str, password: str, level: str, name: str, score: int) -> None: 
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO users (login, password,
                level, name, score) VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                            login, password, level, name, score))
        finally:
            self.connection.close()

    
    def __find_login(self, login: str) -> bool:
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = f"SELECT login FROM users WHERE login = {login}"
                cursor.execute(sql_find_login_query)
                res = self.cursor.fetchone()
                return res != None
        finally:
            self.connection.close()


    def update_users_level(self, login: str, level: str) -> None:
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_update_data_query = """UPDATE tests SET duration = %s, brh_open = %s, brh_cls = %s, before_time = %s,
                status = %s, time_after_start = %s, akb_voltage = %s, press = %s, tank_temp = %s, engine_wall_temp = %s,
                valve_temp = %s, valve_current = %s, heating_current = %s WHERE test_id = %s"""
                cursor.execute(sql_update_data_query, (duration, brh_opn, brh_cls, before_time, status,
                                 time_after_start, akb_voltage, press, tank_temp, engine_wall_temp,
                                 valve_temp, valve_current, heating_current, test_id))
        finally:
            self.connection.close()

    
    def export_data_json(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
            
        finally:
            self.connection.close()
