from view.admin.ClassifyView import ClassifyView
from view.admin.UserManagementView import UserManagementView


class AdminView():
    def __init__(self, user):
        self.user = user

    def start(self):
        while True:
            print("欢迎进入管理员界面")
            print("1.用户管理")
            print("2.植物分类管理")
            print("4. 退出")

            choice = input("请输入选项：")
            if choice == '1':
                UserManagementView(self.user).satrt()
            elif choice == '2':
                ClassifyView(self.user).start()

            elif choice == '4':
                print("退出系统。")
                break
            else:
                print("无效选项，请重新输入。")


if __name__ == '__main__':
    AdminView('admin').start()



