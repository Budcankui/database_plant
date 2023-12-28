from DAO.BaseDAO import BaseDAO
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from model.User import User


class UserDAO(BaseDAO):

    def get_user_by_id(self, user_id):
        sql = text("SELECT * FROM user WHERE user_id = :user_id")
        parameters = {"user_id": user_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return User(*result) if result else None

    def get_user_by_username(self, username):
        sql = text("SELECT * FROM user WHERE username = :username")
        parameters = {"username": username}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return User(*result) if result else None

    def get_all_users(self):
        sql = text("SELECT * FROM user")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [User(*row) for row in result]

    def add_user(self, username, password, role):
        sql = text("INSERT INTO sys_user (username, password, role) VALUES (:username, :password, :role)")
        parameters = {"username": username, "password": password, "role": role}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()  # 提交事务
        return {"username": username, "password": password, "role": role}

    def update_user(self, user_id, new_username):
        sql = text("UPDATE sys_user SET username = :new_username WHERE user_id = :user_id")
        parameters = {"new_username": new_username, "user_id": user_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()  # 提交事务
        return {"user_id": user_id, "username": new_username}

    def delete_user(self, user_id):
        sql = text("DELETE FROM sys_user WHERE user_id = :user_id")
        parameters = {"user_id": user_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()  # 提交事务
        return True


if __name__ == '__main__':
    user_dao = UserDAO()

    res=user_dao.get_all_users()
    print(res)
    # user_dao.add_user("t11t", "test", "哈哈哈")

