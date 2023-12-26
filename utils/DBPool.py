
import pymysql
from dbutils.pooled_db import PooledDB

class MySQLConnectionPool:
    _pool = None

    def __init__(self, max_connections=10):
        self.max_connections = max_connections
        self.config = {
            'host': '182.92.241.41',
            'user': 'root',
            'password': 'zjl1225',
            'database': 'garden_plant'
        }

    def get_connection(self):
        if not self._pool:
            self._pool = PooledDB(
                creator=pymysql,
                maxconnections=self.max_connections,
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['database'],
                cursorclass=pymysql.cursors.DictCursor
            )
        return self._pool.connection()


if __name__ == '__main__':
    pool = MySQLConnectionPool()
    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute('select * from user')
    print(cursor.fetchall())
    cursor.close()
    conn.close()
