from sqlalchemy import text

from DAO.BaseDAO import BaseDAO
from model.monitor import MonitorException


class ExceptionDAO(BaseDAO):

    def get_all(self):
        with self.get_session() as session:
            return session.query(MonitorException).all()