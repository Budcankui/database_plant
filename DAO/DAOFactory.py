from DAO.user.UserDAO import UserDAO


class DAOFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # 在这里进行初始化工作，只会执行一次
            cls._instance._init_factory()
        return cls._instance

    def _init_factory(self):
        # 在这里进行 DAO 工厂的初始化工作
        pass
    @staticmethod
    def get_user_dao():
        return UserDAO()

    # 其他 DAO 的获取方法...

# 示例用法
if __name__ == "__main__":
    dao_factory = DAOFactory()

    # 获取 UserDAO 实例
    user_dao = dao_factory.get_user_dao()
