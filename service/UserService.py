# from DAO.UserDAO import UserDAO
from DAO.DAOFactory import DAOFactory
from DAO.user.UserDAO import UserDAO


class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def login(self, username, password):
        # 调用UserDAO中的方法进行登录验证
        user = self.user_dao.get_user_by_username(username)

        if user and user.password == password:
            return user
        else:
            return None

    def register(self, username, password, role):
        # 先检查用户名是否已存在
        existing_user = self.user_dao.get_user_by_username(username)
        if existing_user:
            print("用户名已存在，请选择其他用户名。")
            return False

        # 调用UserDAO中的方法进行注册
        success = self.user_dao.create_user(username, password, role)
        if success:
            print("注册成功。")
        else:
            print("注册失败，请重试。")

        return success

    def get_user_by_id(self, user_id):
        # 根据用户ID获取用户信息
        return self.user_dao.get_user_by_id(user_id)

    def update_user(self, user_id, new_username, new_password, new_role):
        # 根据用户ID更新用户信息
        success = self.user_dao.update_user(user_id, new_username, new_password, new_role)
        if success:
            print("更新用户信息成功。")
        else:
            print("更新用户信息失败，请重试。")

        return success

    def delete_user(self, user_id):
        # 根据用户ID删除用户
        success = self.user_dao.delete_user(user_id)
        if success:
            print("删除用户成功。")
        else:
            print("删除用户失败，请重试。")

        return success

    def show_all_user(self):
        # 显示所有用户
        users = self.user_dao.get_all_users()
        print("用户列表")
        print("ID\t用户名\t密码\t角色")
        for user in users:
            print(f"{user.user_id}\t{user.username}\t{user.password}\t{user.role}")
        print("按任意键返回")
        input()

    def find_user_by_name(self, user_name):
        return self.user_dao.get_user_by_username(user_name)

    def query_worker_list(self):
        worker_users= self.user_dao.get_worker_list()
        print("ID \t 用户名 \t 角色")
        for user in worker_users:
            print(f"{user.user_id}\t{user.username}\t{user.role}")
        input("按任意键返回")

    def query_monitor_list(self):
        monitor_users= self.user_dao.get_monitor_list()
        print("ID \t 用户名 \t 角色")
        for user in monitor_users:
            print(f"{user.user_id}\t{user.username}\t{user.role}")
        input("按任意键返回")


