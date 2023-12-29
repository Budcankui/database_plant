from sqlalchemy import Column, Integer, DateTime,  Unicode
from datetime import datetime
from sqlalchemy.orm import declarative_base
from DAO.DataSource import DataSource
Base = declarative_base()
class Disease(Base):
    __tablename__ = 'pest_control_disease'
    disease_id = Column(Integer, primary_key=True, autoincrement=True)
    disease_name = Column(Unicode(255, collation='Chinese_PRC_CI_AS'),comment="病虫害名称")
    method = Column(Unicode(255, collation='Chinese_PRC_CI_AS'),comment="防治方法")
    drug = Column(Unicode(255, collation='Chinese_PRC_CI_AS'),comment="药物名称")
    dosage = Column(Unicode(255, collation='Chinese_PRC_CI_AS'),comment="用药量")
    time = Column(Unicode(255, collation='Chinese_PRC_CI_AS'),comment="作用期限")

# 创建表
Base.metadata.create_all(DataSource().engine)



