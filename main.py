from DAO.DAOFactory import DAOFactory
from service.user.UserService import UserService


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
            print("2. 注册")
            print("3. 退出")

            choice = input("请输入选项：")
            if choice == '1':
                username = input("请输入用户名：")
                password = input("请输入密码：")
                self.user = self.user_service.login(username, password)
                if self.user:
                    print(f"登录成功，欢迎 {self.user['username']}({self.user['role']})")
                    # 进入主菜单或其他操作
                    break
                else:
                    print("登录失败，请检查用户名和密码。")

            elif choice == '2':
                username = input("请输入用户名：")
                password = input("请输入密码：")

                # 显示角色选择菜单
                print("角色选择：")
                print("1. 检测人员")
                print("2. 养护人员")
                print("3. 上级主管部门")

                role_choice = input("请选择角色（输入对应的数字）：")
                role_mapping = {'1': '监测人员', '2': '养护人员', '3': '上级主管部门'}
                role = role_mapping.get(role_choice)
                if role:
                    success = self.user_service.register(username, password, role)
                    if success:
                        print("注册成功，请登录。")
                    else:
                        print("注册失败，请重试。")
                else:
                    print("无效的角色选择，请重新注册。")

            elif choice == '3':
                print("退出系统。")
                break

            else:
                print("无效选项，请重新输入。")


if __name__ == "__main__":
    app = GardenPlantApp()
    app.start()
