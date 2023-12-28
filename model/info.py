from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class InfoPlant(Base):
    __tablename__ = 'info_plant'

    plant_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    plant_desc = Column(String(255))
    plant_value = Column(String(255))
    disease_id = Column(Integer)
    created_by = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class InfoImage(Base):
    __tablename__ = 'info_image'

    image_id = Column(Integer, primary_key=True, autoincrement=True)
    plant_id = Column(Integer)
    file_path = Column(String(255))
    image_desc = Column(Integer)
    image_location = Column(String(255))
    image_uploader = Column(Integer)
    created_by = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
