import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DataSource:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_data_source()
        return cls._instance

    def _init_data_source(self):
        db_params = {
            'host': 'rm-bp1a117z150cwqt0lqo.sqlserver.rds.aliyuncs.com',
            'user': 'pubuser',
            'password': '123456!abc',
            'database': 'plant',
            'port': 3433,
        }
        db_connection_string = (
            f"mssql+pymssql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}"
            f"/{db_params['database']}?charset=GBK"
        )
        # print(db_connection_string)
        print(f"Connecting to: {db_connection_string}")
        try:
            self.engine = create_engine(db_connection_string, pool_size=10, max_overflow=5, pool_timeout=30,
                                        pool_recycle=3600)
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise e
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_connection(self):
        return self.engine.connect()

    def close_session(self, session):
        session.close()

    def close_connection(self, connection):
        connection.close()

# 示例用法
if __name__ == '__main__':
    data_source = DataSource()

    # 使用 get_session 方法获取会话
    with data_source.get_session() as session:
        # 执行数据库操作
        pass

    # 使用 get_connection 方法获取连接
    with data_source.get_connection() as connection:
        # 执行数据库操作
        pass
