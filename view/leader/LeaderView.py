from model.User import User
from service.MonitorService import MonitorService
from service.PlantService import PlantService
from service.TaskService import TaskService
from service.UserService import UserService


class  LeaderView():
    def __init__(self,user):
        self.user=user
        self.plant_service=PlantService()
        self.task_service=TaskService()
        self.monitor_service=MonitorService()
        self.user_service = UserService()

    def start(self):
        while True:
            print("欢迎进入上级主管部门界面")
            print("1.查询养护人员信息")
            print("2.查询监护人员信息")
            print("3.分配养护任务")
            print("4.查看养护任务信息")
            print("5.修改养护任务信息")
            print("6.删除养护任务信息")
            print("7.联合查询养护分类植物基本信息")
            print("8.退出")

            choice=input("请输入选项:")
            if choice=='1':
                self.user_service.query_worker_list()
            elif choice=='2':
                self.user_service.query_monitor_list()
            elif choice=='3':
                self.task_service.add_maintenance_task(self.user)
            elif choice=='4':
                self.task_service.query_all_maintenance_task()
            elif choice=='5':
                self.task_service.update_maintenance_task()
            elif choice=='6':
                self.task_service.delete_maintenance_task()
            elif choice=='7':
                self.plant_service.query_plant_join_maintenance_classfiy()
            elif choice=='8':
                print("退出植物信息管理系统。")
                break
            else:
                print("无效选项，请重新输入。")


if __name__ == '__main__':
    user=User(user_id=4)
    LeaderView(user).start()