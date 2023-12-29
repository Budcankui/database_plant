from service.MonitorService import MonitorService


class MonitoringView():
    def __init__(self, user):
        self.user = user
        self.monitor_service = MonitorService()

    def start(self):
        print("欢迎进入监测人员界面")
        while True:
            print("1. 查看监测数据")
            print("2. 上传监测数据")
            print("3. 修改监测数据")
            print("4. 删除监测数据")
            print("5. 查看异常数据")
            print("6. 统计指标最大值、最小值、平均值")
            print("7. 退出")

            choice = input("请输入选项：")
            if choice == '1':
                self.monitor_service.get_all()
            elif choice == '2':
                self.monitor_service.upload_data(self.user)
            elif choice == '3':
                self.monitor_service.update_data(self.user)
            elif choice == '4':
                self.monitor_service.delete_data(self.user)
            elif choice == '5':
                self.monitor_service.get_all_abnormal(self.user)
            elif choice == '6':
                self.monitor_service.get_all_static()
            elif choice == '7':
                print("退出系统。")
                break
            else:
                print("无效选项，请重新输入。")

if __name__ == '__main__':
    from model.User import User
    user = User(user_id=3)
    view = MonitoringView(user)
    view.start()