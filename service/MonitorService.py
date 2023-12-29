from datetime import datetime

from DAO.info.PlantDAO import PlantDAO
from DAO.monitor.DataDAO import DataDAO
from DAO.monitor.ExceptionDAO import ExceptionDAO
from model.User import User
from model.monitor import MonitorData


class MonitorService():
    def __init__(self):
        self.data_dao = DataDAO()
        self.exception_dao = ExceptionDAO()
        self.plant_dao=PlantDAO()

    def get_all(self):
        datas=self.data_dao.get_all()
        print("ID 监测人员ID  监测植物ID  设备名称  温度指标  湿度指标  监测时间")
        for data in datas:
            # 宽度对齐
            print(f"{data.data_id :<5}  {data.user_id :<6}  {data.plant_id :<6}  {data.device_name :<10}  {data.index_temperature :<10}  {data.index_humidity :<10}  {data.monitor_time:10}")

        input("按回车键继续")

    def upload_data(self,user):
        data=MonitorData()
        plant_id=input("请输入监测植物ID：")
        #检验植物是否存在
        if self.plant_dao.get_plant_by_id(plant_id) is None:
            print("植物不存在")
            return
        data.plant_id=plant_id
        data.user_id=user.user_id
        data.device_name=input("请输入设备名称(按回车键跳过)：")
        index_temperature=input("请输入温度(浮点数，按回车键跳过)：")
        data.index_temperature=float(index_temperature) if index_temperature else ""
        index_humidity=input("请输入湿度(浮点数，按回车键跳过)：")
        data.index_humidity=float(index_humidity) if index_humidity else ""
        data.monitor_time=datetime.now()
        self.data_dao.add(data)

    def update_data(self, user):
        datas = self.data_dao.get_all()
        print("ID 监测人员ID  监测植物ID  设备名称  温度指标  湿度指标  监测时间")
        for data in datas:
            print(f"{data.data_id :<5}  {data.user_id :<6}  {data.plant_id :<6}  {data.device_name :<10}  {data.index_temperature :<10}  {data.index_humidity :<10}  {data.monitor_time:10}")

        data_id=input("请输入要修改的监测数据ID：")
        data=self.data_dao.get_data_by_id(data_id)
        if data is None:
            print("监测数据不存在")
            return
        if data.user_id!=user.user_id:
            print("无权修改")
            return
        device_name=input("请输入新的设备名称(按回车键跳过)：")
        if device_name:
            data.device_name=device_name
        index_temperature=input("请输入新的温度(浮点数，按回车键跳过)：")
        if index_temperature:
            data.index_temperature=float(index_temperature)
        index_humidity=input("请输入新的湿度(浮点数，按回车键跳过)：")
        if index_humidity:
            data.index_humidity=float(index_humidity)
        data.monitor_time=datetime.now()
        self.data_dao.update(data)

    def delete_data(self, user):
        data_id=input("请输入要删除的监测数据ID：")
        data=self.data_dao.get_data_by_id(data_id)
        if data is None:
            print("监测数据不存在")
            return
        if data.user_id!=user.user_id:
            print("无权删除")
            return
        self.data_dao.delete(data)

    def get_all_abnormal(self, user):
        err_datas=self.exception_dao.get_all()
        print("ID 监测人员ID  检测数据ID  异常指标  异常值")
        for err_data in err_datas:
            print(f"{err_data.exception_id :<5}   {err_data.data_id :<6}  {err_data.exception_index :<10}  {err_data.exception_value :<10}")

    def get_all_static(self):
        res=self.data_dao.get_static()
        print("       最大值  最小值  温平均值")
        print(f"温度    {res.max_temperature :<10}  {res.min_temperature :<10}  {res.avg_temperature :<10}")
        print(f"湿度    {res.max_humidity :<10}  {res.min_humidity :<10}  {res.avg_humidity :<10}")



if __name__ == '__main__':
    user=User(user_id=3)
    service = MonitorService()
    # service.get_all()
    service.upload_data(user)