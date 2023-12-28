from sqlalchemy import Column, Integer, String, Unicode, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base
from DAO.DataSource import DataSource

Base = declarative_base()

class ClassifyFamily(Base):
    __tablename__ = 'classify_family'

    family_id = Column(Integer, primary_key=True, autoincrement=True)
    family_name = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), nullable=False)
    created_by = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class ClassifyGenus(Base):
    __tablename__ = 'classify_genus'

    genus_id = Column(Integer, primary_key=True, autoincrement=True)
    genus_name = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), nullable=False)
    family_id = Column(Integer)
    created_by = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class ClassifySpecies(Base):
    __tablename__ = 'classify_species'

    species_id = Column(Integer, primary_key=True, autoincrement=True)
    genus_id = Column(Integer)
    species_name = Column(Unicode(255, collation='Chinese_PRC_CI_AS'), nullable=False)
    species_alias = Column(Unicode(255, collation='Chinese_PRC_CI_AS'))
    growth_env = Column(Unicode(255, collation='Chinese_PRC_CI_AS'))
    province = Column(Unicode(255, collation='Chinese_PRC_CI_AS'))
    city = Column(Unicode(255, collation='Chinese_PRC_CI_AS'))
    country = Column(Unicode(255, collation='Chinese_PRC_CI_AS'))
    created_by = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

# 创建表
Base.metadata.create_all(DataSource().engine)
