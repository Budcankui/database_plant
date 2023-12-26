from utils.DBPool import MySQLConnectionPool


class BaseDAO:
    def __init__(self):
        self.connection = None

    def open_connection(self):
        pool = MySQLConnectionPool()
        self.connection = pool.get_connection()

    def close_connection(self):
        if self.connection:
            self.connection.close()