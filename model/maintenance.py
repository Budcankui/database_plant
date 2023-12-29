from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import declarative_base

from DAO.DataSource import DataSource

Base = declarative_base()
class Task(Base):
    __tablename__ = 'maintenance_task'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    plant_id = Column(Integer, comment='植物id')
    user_id = Column(Integer, comment='养护人人员id')
    task_name = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="任务名称")
    task_time = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="执行时间")
    task_location= Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="执行地点")
    task_desc= Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="任务描述")
    task_status=  Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="任务状态")

# 创建表
Base.metadata.create_all(DataSource().engine)