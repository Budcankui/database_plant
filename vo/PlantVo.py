# models.py

from sqlalchemy import Column, Unicode, Integer, MetaData, Table
from sqlalchemy.orm import declarative_base

Base = declarative_base()

metadata = MetaData()

plant_info_view = Table(
    'PlantInfoView',
    metadata,
    Column('plant_id', Integer, primary_key=True, comment='植物ID'),
    Column('family_name', Unicode, comment='科名'),
    Column('genus_name', Unicode, comment='属名'),
    Column('species_name', Unicode, comment='种名'),
    Column('disease_name', Unicode, comment='病虫害名称'),
    Column('disease_control_method', Unicode, comment='防治方法'),
    Column('plant_desc', Unicode, comment='形态特征'),
    Column('plant_value', Unicode, comment='应用价值'),
    Column('plant_tip', Unicode, comment='栽培要点'),
    Column('image_path', Unicode, comment='图片文件路径'),
    Column('image_desc', Unicode, comment='配图描述'),
    Column('image_location', Unicode, comment='拍摄地点'),
)

class PlantVO(Base):
    __table__ = plant_info_view
