
from DAO.info.DistributionDao import DistributionDao



class DaoFactory:
    @staticmethod
    def get_distribution_dao() -> DistributionDao:
        # 在此可以根据需要返回不同的 DAO 实现类
        return DistributionDao()

if __name__ == '__main__':

    # 使用示例
    dao_impl = DaoFactory.get_distribution_dao()
    result = dao_impl.get_distribution_by_id(1)
    print(result)