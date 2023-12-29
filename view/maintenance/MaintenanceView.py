from model.User import User
from service.DiseaseService import DiseaseService
from service.TaskService import TaskService


class MaintenanceView():
    def __init__(self, user):
        self.user = user
        self.disease_service = DiseaseService()
        self.task_service = TaskService()


    def start(self):
        print("欢迎进入养护人员界面")
        while True:
            print("1. 病虫害信息管理")
            print("2. 养护任务管理")
            print("3. 退出")

            choice = input("请输入选项：")
            if choice == '1':
                self.disease_view()
            elif choice == '2':
                self.task_view()
            elif choice == '3':
                print("退出系统。")
                break

    def disease_view(self):
        while True:
            print("1. 查看病虫害信息")
            print("2. 添加病虫害信息")
            print("3. 修改病虫害信息")
            print("4. 删除病虫害信息")
            print("5. 退出")

            choice = input("请输入选项：")
            if choice == '1':
                self.disease_service.get_all()
            elif choice == '2':
                self.disease_service.add()
            elif choice == '3':
                self.disease_service.update()
            elif choice == '4':
                self.disease_service.delete()
            elif choice == '5':
                print("退出系统。")
                break
            else:
                print("无效选项，请重新输入。")

    def task_view(self):
        while True:
            print("1. 查看个人养护任务")
            print("2. 提交完成养护任务")
            print("3. 查询已完成养护任务")
            print("4. 退出")
            choice = input("请输入选项：")
            if choice == '1':
                self.task_service.get_worker_todo_task(self.user)
            elif choice == '2':
                self.task_service.update_worker_done_task(self.user)
            elif choice == '3':
                self.task_service.get_worker_done_task(self.user)
            elif choice == '4':
                print("退出系统。")
                break
            else:
                print("无效选项，请重新输入。")


if __name__ == '__main__':
    MaintenanceView(User(user_id=2)).start()