from sqlalchemy import text, desc, func

from DAO.BaseDAO import BaseDAO
from model.monitor import MonitorData


class DataDAO(BaseDAO):

    def get_all(self):
        with self.get_session() as session:
            return session.query(MonitorData).order_by(desc(MonitorData.monitor_time)).all()

    def add(self, data):
        with self.get_session() as session:
            session.add(data)
            session.commit()

    def get_data_by_id(self, data_id):
        with self.get_session() as session:
            return session.query(MonitorData).filter(MonitorData.data_id == data_id).first()

    def update(self, data):
        with self.get_session() as session:
            session.merge(data)
            session.commit()

    def delete(self, data):
        with self.get_session() as session:
            session.delete(data)
            session.commit()


    def get_static(self):
        with self.get_session() as session:
            # 查询最大值、最小值和平均值
            result = session.query(func.max(MonitorData.index_humidity).label('max_humidity'),
                                    func.min(MonitorData.index_humidity).label('min_humidity'),
                                    func.avg(MonitorData.index_humidity).label('avg_humidity'),
                                    func.max(MonitorData.index_temperature).label('max_temperature'),
                                    func.min(MonitorData.index_temperature).label('min_temperature'),
                                    func.avg(MonitorData.index_temperature).label('avg_temperature')).first()
            return  result
