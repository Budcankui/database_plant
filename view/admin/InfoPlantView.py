from service.PlantService import PlantService


class InfoPlantView():
    def __init__(self, user):
        self.user = user
        self.plant_service = PlantService()

    def start(self):
        while True:
            print("1. 查询植物信息")
            print("2. 增加植物信息")
            print("3. 修改植物信息")
            print("4. 删除植物信息")
            print("5. 联合查询植物视图详细信息")
            print("6. 统计每科植物数量")
            print("7. 根据任意个数属性组合物查询植物信息")
            print("8. 退出")

            choice = input("请输入选项：")

            if choice == '1':
                self.view_plant_list()
            elif choice == '2':
                self.add_plant()
            elif choice == '3':
                self.update_plant()
            elif choice == '4':
                self.delete_plant()
            elif choice == '5':
                self.plant_service.query_plant_detail_view()
            elif choice == '6':
                self.plant_service.query_plant_count_by_family()
            elif choice == '7':
                self.plant_service.query_plant_by_attribute()
            elif choice == '8':
                print("退出植物信息管理系统。")
                break
            else:
                print("无效选项，请重新输入。")

    def view_plant_list(self):
        self.plant_service.query_plant_list()

    def add_plant(self):
        self.plant_service.add_plant(self.user)

    def update_plant(self):
        self.plant_service.update_plant(self.user)

    def delete_plant(self):
        self.plant_service.delete_plant()


if __name__ == '__main__':
    InfoPlantView('admin').start()
