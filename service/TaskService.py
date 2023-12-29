

from DAO.maintenance.TaskDAO import TaskDAO


class TaskService():
    def __init__(self):
        self.task_dao = TaskDAO()

    def get_worker_todo_task(self, user):
        tasks=self.task_dao.get_worker_todo_task(user)
        print("ID 植物ID 养护人员ID 任务名称 执行时间 执行地点 任务描述 任务状态")
        for task in tasks:
            print(task.task_id,task.plant_id,task.user_id,task.task_name,task.task_time,task.task_location,task.task_desc,task.task_status)

    def get_worker_done_task(self, user):
        tasks=self.task_dao.get_worker_done_task(user)
        print("ID 植物ID 养护人员ID 任务名称 执行时间 执行地点 任务描述 任务状态")
        for task in tasks:
            print(task.task_id,task.plant_id,task.user_id,task.task_name,task.task_time,task.task_location,task.task_desc,task.task_status)

    def update_worker_done_task(self, user):
        self.get_worker_todo_task(user)
        task_id = input("请输入完成的任务ID(按回车退出)：")
        #检查任务是否存在
        task=self.task_dao.get_task_by_id(task_id)
        if task is None:
            print("任务不存在")
            return

        task.task_status = "已完成"
        self.task_dao.update_status(task)
        print("任务已完成。")



        