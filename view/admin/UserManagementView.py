from service.UserService import UserService


class UserManagementView():
    def __init__(self,user):
        self.user = user
        self.user_service = UserService()

    def satrt(self):
        while True:
            print("欢迎进入用户管理界面")
            print("1.查看用户")
            print("2.添加用户")
            print("3.修改用户")
            print("4.删除用户")
            print("5.退出")

            choice = input("请输入选项：")
            if choice == '1':
                self.show_all_user()
            elif choice == '2':
                self.add_user()
            elif choice == '3':
                self.update_user()
            elif choice == '4':
                self.delete_user()
            elif choice == '5':
                print("退出系统。")
                break
            else:
                print("无效选项，请重新输入。")

    def show_all_user(self):
        self.user_service.show_all_user()

    def add_user(self):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        # 输入数字选择三种角色之一 leader monitor worker
        print("请选择角色：")
        print("1. 上级主管部门")
        print("2. 监测人员")
        print("3. 养护人员")
        role = input("请输入选项：")
        if role == '1':
            role = '上级主管部门'
        elif role == '2':
            role = '监测人员'
        elif role == '3':
            role = '养护人员'
        else:
            print("无效选项，请重新输入。")
            return
        self.user_service.register(username,password,role)
        print("添加用户成功。")

    def update_user(self):
        user_name = input("请输入要修改信息的用户名称：")
        # 检测用户是否存在
        user = self.user_service.find_user_by_name(user_name)
        if user is None:
            print("用户不存在")
            return

        print(f"用户信息：{user}")

        new_username = input("是否要更新用户名？(按回车跳过): ")
        new_username = new_username if new_username != '' else user.username

        new_password = input("是否要更新密码？(按回车跳过): ")
        new_password = new_password if new_password != '' else user.password

        update_role = input("是否要更新角色？(leader/monitor/worker，按回车跳过): ")
        if update_role != '':
            while update_role not in ['leader', 'monitor', 'worker']:
                print("无效的角色选项，请重新输入。")
                update_role = input("是否要更新角色？(leader/monitor/worker，按回车跳过): ")
            new_role = update_role
        else:
            new_role = user.role

        # 调用更新用户信息的方法，传递需要更新的字段
        self.user_service.update_user(user.user_id, new_username, new_password, new_role)
        print("更新用户信息成功。")

    def delete_user(self):
        user_name = input("请输入要删除的用户名称：")
        # 检测用户是否存在
        user = self.user_service.find_user_by_name(user_name)
        if user is None:
            print("用户不存在")
            return

        # 确认是否删除用户
        confirm = input(f"确认要删除用户 {user_name} 吗？ (y/n): ")
        if confirm.lower() != 'y':
            print("取消删除操作。")
            return

        # 调用删除用户的方法
        self.user_service.delete_user(user.user_id)
        print("删除用户成功。")




