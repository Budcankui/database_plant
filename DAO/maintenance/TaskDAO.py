from sqlalchemy.orm import Session
from sqlalchemy import text

from DAO.BaseDAO import BaseDAO
from model.User import User
from model.maintenance import Task


class TaskDAO(BaseDAO):

    def add_task(self, plant_id, user_id, task_name, task_time, task_location, task_desc, task_status):
        sql = text("INSERT INTO maintenance_task (plant_id, user_id, task_name, task_time, task_location, task_desc, task_status) "
                   "VALUES (:plant_id, :user_id, :task_name, :task_time, :task_location, :task_desc, :task_status)")
        parameters = {
            "plant_id": plant_id,
            "user_id": user_id,
            "task_name": task_name,
            "task_time": task_time,
            "task_location": task_location,
            "task_desc": task_desc,
            "task_status": task_status
        }
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"plant_id": plant_id, "user_id": user_id, "task_name": task_name,
                "task_time": task_time, "task_location": task_location, "task_desc": task_desc, "task_status": task_status}

    def get_all_tasks(self):
        sql = text("SELECT * FROM maintenance_task")
        with self.get_session() as session:
            result = session.execute(sql).fetchall()
        return [self._map_result_to_task(row) for row in result]

    def get_task_by_user_id(self, user_id):
        sql = text("SELECT * FROM maintenance_task WHERE user_id = :user_id ")
        parameters = {"user_id": user_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchall()
        return [self._map_result_to_task(row) for row in result]

    def get_task_by_id(self, task_id):
        sql = text("SELECT * FROM maintenance_task WHERE task_id = :task_id")
        parameters = {"task_id": task_id}
        with self.get_session() as session:
            result = session.execute(sql, parameters).fetchone()
        return self._map_result_to_task(result)

    def update_task(self, task_id, updated_plant_id, updated_user_id, updated_task_name,
                    updated_task_time, updated_task_location, updated_task_desc, updated_task_status):
        sql = text("UPDATE maintenance_task SET "
                   "plant_id = :updated_plant_id, user_id = :updated_user_id, "
                   "task_name = :updated_task_name, task_time = :updated_task_time, "
                   "task_location = :updated_task_location, task_desc = :updated_task_desc, "
                   "task_status = :updated_task_status "
                   "WHERE task_id = :task_id")
        parameters = {
            "task_id": task_id,
            "updated_plant_id": updated_plant_id,
            "updated_user_id": updated_user_id,
            "updated_task_name": updated_task_name,
            "updated_task_time": updated_task_time,
            "updated_task_location": updated_task_location,
            "updated_task_desc": updated_task_desc,
            "updated_task_status": updated_task_status
        }
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return {"task_id": task_id, "plant_id": updated_plant_id, "user_id": updated_user_id,
                "task_name": updated_task_name, "task_time": updated_task_time,
                "task_location": updated_task_location, "task_desc": updated_task_desc, "task_status": updated_task_status}

    def delete_task(self, task_id):
        sql = text("DELETE FROM maintenance_task WHERE task_id = :task_id")
        parameters = {"task_id": task_id}
        with self.get_session() as session:
            session.execute(sql, parameters)
            session.commit()
        return True

    def _map_result_to_task(self, result):
        if result:
            return Task(
                task_id=result[0],
                plant_id=result[1],
                user_id=result[2],
                task_name=result[3],
                task_time=result[4],
                task_location=result[5],
                task_desc=result[6],
                task_status=result[7]
            )
        return None

    def get_worker_todo_task(self, user):
        # 使用sqlalchemy的session
        with self.get_session() as session:
             # 使用sqlalchemy的text方法，可以直接使用sql语句
            todo_tasks=session.query(Task).filter(Task.user_id == user.user_id, Task.task_status == "未完成").all()
            return todo_tasks

    def get_worker_done_task(self, user):
        with self.get_session() as session:
            done_tasks=session.query(Task).filter(Task.user_id == user.user_id, Task.task_status == "已完成").all()
            return done_tasks

    def update_status(self, task):
        with self.get_session() as session:
            session.query(Task).filter(Task.task_id == task.task_id).update({Task.task_status: task.task_status})
            session.commit()


if __name__ == '__main__':

    task_dao = TaskDAO()
    task_dao.get_worker_todo_task(User(user_id=2))