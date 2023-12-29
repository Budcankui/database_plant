from DAO.info.PlantDAO import PlantDAO
from DAO.maintenance.TaskDAO import TaskDAO
from DAO.user.UserDAO import UserDAO
from model.maintenance import Task


class TaskService():
    def __init__(self):
        self.task_dao = TaskDAO()
        self.user_dao = UserDAO()
        self.plant_dao = PlantDAO()

    def print_all_tasks(self,tasks):
        print("ID 植物ID 养护人员ID 任务名称 执行时间 执行地点 任务描述 任务状态")
        for task in tasks:
            print(task.task_id,task.plant_id,task.user_id,task.task_name,task.task_time,task.task_location,task.task_desc,task.task_status)

    def get_worker_todo_task(self, user):
        tasks=self.task_dao.get_worker_todo_task(user)
        self.print_all_tasks(tasks)

    def get_worker_done_task(self, user):
        tasks=self.task_dao.get_worker_done_task(user)
        self.print_all_tasks(tasks)

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

    def add_maintenance_task(self, user):
        task = Task()
        worker_id = input("请输养护人员ID：")
        # 检验养护人员是否存在
        if self.user_dao.get_by_id_and_role(worker_id,"养护人员") is None:
            print("养护人员不存在")
            return
        task.user_id = worker_id
        plant_id = input("请输入监测植物ID：")
        # 检验植物是否存在
        if self.plant_dao.get_plant_by_id(plant_id) is None:
            print("植物不存在")
            return
        task.plant_id = plant_id
        task.task_name = input("请输入任务名称：")
        task.task_location = input("请输入任务位置：")
        task.task_time = input("请输入任务执行时间：")
        task.task_desc = input("请输入任务描述：")
        task.task_status = "未完成"
        self.task_dao.add(task)

    def query_all_maintenance_task(self):
        tasks = self.task_dao.get_all_tasks()
        self.print_all_tasks(tasks)
        input("按回车键继续")

    def update_maintenance_task(self):
        task=Task()
        task_id = input("请输入要修改的任务ID：")
        # 检查任务是否存在
        if self.task_dao.get_task_by_id(task_id) is None:
            print("任务不存在")
            return
        task.task_id = task_id
        user_id = input("请输养护人员ID：")
        # 检验养护人员是否存在
        if self.user_dao.get_by_id_and_role(user_id, "养护人员") is None:
            print("养护人员不存在")
            return
        task.user_id = user_id
        plant_id = input("请输入监测植物ID：")
        # 检验植物是否存在
        if self.plant_dao.get_plant_by_id(plant_id) is None:
            print("植物不存在")
            return
        task.plant_id = plant_id
        task_name = input("请输入任务名称(按回车跳过)：")
        if task_name != "":
            task.task_name = task_name
        task_location = input("请输入任务位置(按回车跳过)：")
        if task_location != "":
            task.task_location = task_location
        task_desc = input("请输入任务描述(按回车跳过)：")
        if task_desc != "":
            task.task_desc = task_desc
        task_time = input("请输入任务执行时间(按回车跳过)：")
        if task_time != "":
            task.task_time = task_time
        self.task_dao.update(task)
        print("任务已修改。")

    def delete_maintenance_task(self):
        task_id = input("请输入要删除的任务ID：")
        # 检查任务是否存在
        if self.task_dao.get_task_by_id(task_id) is None:
            print("任务不存在")
            return
        self.task_dao.delete(task_id)
        print("任务已删除。")





        