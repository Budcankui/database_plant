from sqlalchemy import Column, Integer, Float, DateTime, Unicode, ForeignKey, text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

from DAO.DataSource import DataSource

Base = declarative_base()

class MonitorData(Base):
    __tablename__ = 'monitor_data'
    # 解决触发器output报错
    __table_args__ = {'implicit_returning': False}
    data_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, comment='监测人员id')
    plant_id = Column(Integer, nullable=False, comment='监测植物id')
    device_name = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment='设备名称')
    index_temperature = Column(Float, comment='温度指标')
    index_humidity = Column(Float, comment='湿度指标')
    monitor_time = Column(DateTime, default=datetime.now, comment='监测时间')



class MonitorException(Base):
    __tablename__ = 'monitor_exception'

    exception_id = Column(Integer, primary_key=True, autoincrement=True)
    data_id = Column(Integer, nullable=False, comment='异常监测数据id')
    exception_index = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment='异常指标')
    exception_value = Column(Float, comment='异常指标数据')

#创建表
Base.metadata.create_all(DataSource().engine)

