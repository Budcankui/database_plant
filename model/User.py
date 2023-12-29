
from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'sys_user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Unicode(32))
    password = Column(String(32))
    role = Column(Unicode(32))

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, role={self.role})>"
