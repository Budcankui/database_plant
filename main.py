from DAO.DAOFactory import DAOFactory
from service.UserService import UserService
from view.admin.AdminView import AdminView
from view.maintenance.MaintenanceView import MaintenanceView
from view.monitor.MonitorView import MonitoringView


class GardenPlantApp:
    def __init__(self):
        self.user_service = UserService()
        self.user_dao = DAOFactory.get_user_dao()
        self.user = None

    def start(self):
        self.login()

    def login(self):
        while True:
            print("登录系统")
            print("1. 登录")
            print("2. 退出")

            choice = input("请输入选项：")
            if choice == '1':
                username = input("请输入用户名：")
                password = input("请输入密码：")
                self.user = self.user_service.login(username, password)
                if self.user:
                    print(f"登录成功，欢迎 {self.user.username}({self.user.role})")
                    # 根据角色跳转到不同的界面
                    if self.user.role == 'admin':
                        AdminView(self.user).start()
                    elif self.user.role == '养护人员':
                        MaintenanceView(self.user).start()
                    elif self.user.role == '监测人员':
                        MonitoringView(self.user).start()
                    elif self.user.role == '上级主管部门':
                        LeaderView(self.user).start()

                else:
                    print("登录失败，请检查用户名和密码。")

            elif choice == '2':
                print("退出系统。")
                break

            else:
                print("无效选项，请重新输入。")


if __name__ == "__main__":
    app = GardenPlantApp()
    app.start()
