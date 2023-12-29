from sqlalchemy import Column, Integer, String, DateTime,  Unicode

from datetime import datetime
from sqlalchemy.orm import declarative_base

from DAO.DataSource import DataSource

Base = declarative_base()

class Plant(Base):
    __tablename__ = 'info_plant'

    plant_id = Column(Integer, primary_key=True, autoincrement=True)
    species_id = Column(Integer,comment='物种id')
    disease_id = Column(Integer,comment='病虫害id')
    plant_desc = Column(Unicode(255, collation='Chinese_PRC_CI_AS'),comment="形态特征")
    plant_value = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="应用价值")
    plant_tip = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="栽培要点")
    image_path = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="图片文件路径")
    image_desc = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="配图描述")
    image_location = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), comment="拍摄地点")
    create_by = Column(Integer,comment="配图拍摄人")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
# 创建表
Base.metadata.create_all(DataSource().engine)



