from sqlalchemy.orm import Session

from DAO.DataSource import DataSource


class BaseDAO:
    def __init__(self):
        self.data_source = DataSource()



    def get_session(self) -> Session:
        return self.data_source.get_session()

    def get_connection(self):
        return self.data_source.get_connection()

    def __enter__(self):
        # 进入上下文时，创建一个 session 并返回
        self.session = self.Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 退出上下文时，关闭 session
        self.session.close()
