import psycopg2


class DB:
    def DB_connect(self):
        self.connection = psycopg2.connect(dbname='database', 
                                    user='postgres', 
                                    password='$NS$//1907',
                                    host='localhost')


    def __init__(self):
        self.DB_connect()
        self.connection.close()

    def create_table(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_create_tb_test_data_query = """CREATE TABLE IF NOT EXISTS tests_data (
                    test_id BIGSERIAL PRIMARY KEY, 
                    time_after_start INTEGER, 
                    akb_voltage DOUBLE PRECISION, 
                    pressure DOUBLE PRECISION, 
                    tank_temp DOUBLE PRECISION, 
                    engine_wall_temp DOUBLE PRECISION, 
                    valve_temp DOUBLE PRECISION, 
                    valve_current DOUBLE PRECISION, 
                    heating_current DOUBLE PRECISION)"""

                cursor.execute(sql_create_tb_test_data_query)
                
                sql_create_tb_test_descr_query = """CREATE TABLE IF NOT EXISTS tests_descr (
                    test_id INTEGER PRIMARY KEY,
                    duration INTEGER, 
                    brh_opn INTEGER, 
                    brh_cls INTEGER, 
                    before_time INTEGER, 
                    status BOOLEAN)"""
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

    def insert_data(self, test_id, time_after_start, akb_voltage, press, tank_temp, engine_wall_temp, valve_temp,
                valve_current, heating_current):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO tests_data (test_id, time_after_start,
                akb_voltage, pressure, tank_temp, engine_wall_temp, valve_temp,
                valve_current, heating_current) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                            test_id, time_after_start, akb_voltage, press, tank_temp, engine_wall_temp,
                            valve_temp, valve_current, heating_current))
        finally:
            self.connection.close()

    
    def update_data(self, test_id, duration, brh_opn, brh_cls, before_time, status,
                time_after_start, akb_voltage, press, tank_temp, engine_wall_temp,
                valve_temp, valve_current, heating_current):
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
