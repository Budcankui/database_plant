from datetime import datetime

from DAO.DAOFactory import DAOFactory
from model.info.Plant import Plant
from model.info.PlantImage import PlantImage
from model.info.Taxonomy import Taxonomy


class InfoService:
    welcome = "欢迎来到 园林植物基本信息管理业务 模块"
    options = """
        1.查看植物信息
        2.查询并修改植物信息
        3.删除植物信息
        4.添加植物
        5.统计每科植物的数量
        6.根据属性、属性组合查询植物
    """

    def __init__(self):
        pass

    def service(self):
        input = input
        print(self.welcome)
        print(self.options)

        choice = input("请输入选项：")
        if choice == "1":
            self.get_first_5_plants()
        elif choice == "2":
            self.search_and_modify()
        elif choice == "3":
            self.delete_plant()
        elif choice == "4":
            self.add_plant()
        elif choice == "5":
            self.analyse_family()
        elif choice == "6":
            self.search_by_multiple_params()
        else:
            print("输入错误")

    def add_plant(self):
        taxonomy = Taxonomy()
        print("请输入植物的科名")
        taxonomy.family = input()

        print("请输入植物的属名")
        taxonomy.genus = input()

        print("请输入植物的种名")
        taxonomy.species = input()

        plant = Plant()

        print("请您输入病名")
        plant.disease_name = input()

        print("请您输入植物的别名")
        plant.common_name = input()

        print("请您输入植物的形态特征")
        plant.morphology = input()

        print("请您输入植物的栽培技术要点")
        plant.cultivation_tips = input()

        print("请您输入病虫害防治措施")
        plant.pest_control_measures = input()

        print("请您输入植物的应用价值")
        plant.application_value = input()

        print("请您输入创建者姓名")
        plant.creator = input()

        # 设置创建时间和更新时间
        plant.create_time = datetime.now()
        plant.update_time = datetime.now()

        print("请输入植物图片的路径：")
        image = PlantImage()
        image.photo_path = input()

        print("请输入植物图片的拍摄人：")
        image.photographer = input()

        print("请输入植物图片的拍摄地点：")
        image.location = input()

        print("请输入植物图片的描述信息：")
        image.description = input()

        plant_dao = DAOFactory.get_plant_dao()
        plant_dao.add_plant(plant)

        taxonomy.plant_id = plant.plant_id
        image.plant_id = plant.plant_id

        taxonomy_dao = DAOFactory.get_taxonomy_dao()
        taxonomy_dao.add_taxonomy(taxonomy)

        image_dao = DAOFactory.get_image_dao()
        image_dao.add_image(image)

    def get_first_5_plants(self):
        plant_dao = DAOFactory.get_plant_dao()
        plants = plant_dao.get_all_plants()
        self.print_plant_info(self.get_full_plant_info_by_plant(plants))
        if not plants:
            print("数据库为空，您可以先添加数据")

    def search_and_modify(self):
        print("请输入植物的种名")
        name = input()

        taxonomy_dao = DAOFactory.get_taxonomy_dao()
        plant_dao = DAOFactory.get_plant_dao()
        plant_image_dao = DAOFactory.get_image_dao()

        taxonomy = taxonomy_dao.get_taxonomy_by_species(name)
        if not taxonomy:
            print("您查找的植物不存在")
            return

        plant = plant_dao.get_plant_by_id(taxonomy.plant_id)

        print("""
            可修改的信息如下：
            1.植物的病名
            2.植物的别名
            3.植物的形态特征
            4.植物的栽培技术要点
            5.植物的病虫害防治措施
            6.植物的应用价值
            7.植物的科名
            8.植物的属名
            9.植物的种名
        """)

        choice = input()
        if choice == "1":
            print("请输入新信息：")
            plant.disease_name = input()
        elif choice == "2":
            print("请输入新信息：")
            plant.common_name = input()
        elif choice == "3":
            print("请输入新信息：")
            plant.morphology = input()
        elif choice == "4":
            print("请输入新信息：")
            plant.cultivation_tips = input()
        elif choice == "5":
            print("请输入新信息：")
            plant.pest_control_measures = input()
        elif choice == "6":
            print("请输入新信息：")
            plant.application_value = input()
        elif choice == "7":
            print("请输入新信息：")
            taxonomy.family = input()
        elif choice == "8":
            print("请输入新信息：")
            taxonomy.genus = input()
        elif choice == "9":
            print("请输入新信息：")
            taxonomy.species = input()
        else:
            print("输入有误")
            return

        taxonomy_updated = taxonomy_dao.update_taxonomy(taxonomy)
        plant_updated = plant_dao.update_plant(plant)

        if taxonomy_updated and plant_updated:
            print("更新完成")
        else:
            print("出现错误，更新失败")

    def delete_plant(self):
        print("您可以通过 1.植物的ID 2.植物的种名 来删除植物的信息")

        choice = input()
        if choice == "1":
            try:
                print("请输入信息：")
                plant_id = int(input())
                plant_dao = DAOFactory.get_plant_dao()
                taxonomy_dao = DAOFactory.get_taxonomy_dao()
                plant_image_dao = DAOFactory.get_image_dao()

                taxonomy_deleted = taxonomy_dao.delete_taxonomy_by_plant_id(plant_id)
                plant_deleted = plant_dao.delete_plant(plant_id)
                image_deleted = plant_image_dao.delete_image_by_plant_id(plant_id)

                if taxonomy_deleted and plant_deleted and image_deleted:
                    print("删除成功")
                else:
                    print("删除失败")
            except ValueError:
                print("输入错误")
                return
        elif choice == "2":
            print("请输入信息：")
            species = input()
            plant_dao = DAOFactory.get_plant_dao()
            taxonomy_dao = DAOFactory.get_taxonomy_dao()
            plant_image_dao = DAOFactory.get_image_dao()

            taxonomy = taxonomy_dao.get_taxonomy_by_species(species)
            if not taxonomy:
                print("您查找的植物不存在")
                return

            taxonomy_deleted = taxonomy_dao.delete_taxonomy_by_plant_id(taxonomy.plant_id)
            plant_deleted = plant_dao.delete_plant(taxonomy.plant_id)
            image_deleted = plant_image_dao.delete_image_by_plant_id(taxonomy.plant_id)

            if taxonomy_deleted and plant_deleted and image_deleted:
                print("删除成功")
            else:
                print("删除失败")
        else:
            print("输入错误。")

    def analyse_family(self):
        taxonomy_dao = DAOFactory.get_taxonomy_dao()
        families = taxonomy_dao.get_all_family()
        print("所有的科名：", end=" ")
        print(*families)

        print("请您输入想要查找的科名植物")
        family_name = input()

        if family_name in families:
            taxonomy_dao.create_view(family_name)
            sql = f"select * from {family_name}_view"
            taxonomy_list = taxonomy_dao.get_taxonomy_by_single_param(sql)

            for taxonomy in taxonomy_list:
                print(f"plantID:{taxonomy.plant_id} 种名:{taxonomy.species} 科名:{taxonomy.family}")

    def search_by_multiple_params(self):
        print("您可以选择 1.单个属性查找 2.多属性查找")
        option = input()
        if option == "1":
            print("""
                可查找的属性如下：
                1.植物的病名
                2.植物的别名
                3.植物的形态特征
                4.植物的栽培技术要点
                5.植物的病虫害防治措施
                6.植物的应用价值
                7.植物的科名
                8.植物的属名
                9.植物的种名
            """)
            param_num = input()

            if param_num in {"1", "2", "3", "4", "5", "6"}:
                print("请输入关键词：")
                keyword = input()
                param = self.get_param(int(param_num))
                sql = f"SELECT * FROM plant where {param} = '{keyword}'"

                plant_dao = PlantDAOImpl()
                plant_list = plant_dao.get_plant_by_single_param(sql)
                self.print_plant_info(self.get_full_plant_info_by_plant(plant_list))
            elif param_num in {"7", "8", "9"}:
                print("请输入关键词：")
                keyword = input()
                param = self.get_param(int(param_num))
                sql = f"SELECT * FROM taxonomy where {param} = '{keyword}'"

                taxonomy_dao = TaxonomyDAOImpl()
                taxonomy_list = taxonomy_dao.get_taxonomy_by_single_param(sql)
                self.print_plant_info(self.get_full_plant_info_by_taxonomy(taxonomy_list))
            else:
                print("输入有误")
        elif option == "2":
            print("您可以通过一对属性来进行筛选")

            print("""
                第一个属性
                1.植物的病名
                2.植物的别名
                3.植物的形态特征
                4.植物的栽培技术要点
                5.植物的病虫害防治措施
                6.植物的应用价值
                7.植物的科名
                8.植物的属名
                9.植物的种名
            """)

            first_param_num = input()
            try:
                first_param_num = int(first_param_num)
            except ValueError:
                print("输入错误")
                return

            if first_param_num in {1, 2, 3, 4, 5, 6}:
                print("""
                    第二个属性
                    1.植物的病名
                    2.植物的别名
                    3.植物的形态特征
                    4.植物的栽培技术要点
                    5.植物的病虫害防治措施
                    6.植物的应用价值
                """)

                second_param_num = input()
                try:
                    second_param_num = int(second_param_num)
                except ValueError:
                    print("输入错误")
                    return

                print("请输入第一个参数")
                first_value = input()
                print("请输入第二个参数")
                second_value = input()

                first_param = self.get_param(first_param_num)
                second_param = self.get_param(second_param_num)

                if first_param and second_param:
                    if first_param_num <= 6:
                        sql = f"select * from plant where {first_param} = '{first_value}' and {second_param} = '{second_value}'"
                        plant_dao = PlantDAOImpl()
                        plant_list = plant_dao.get_plant_by_single_param(sql)
                        self.print_plant_info(self.get_full_plant_info_by_plant(plant_list))
                    else:
                        sql = f"select * from taxonomy where {first_param} = '{first_value}' and {second_param} = '{second_value}'"
                        taxonomy_dao = TaxonomyDAOImpl()
                        taxonomy_list = taxonomy_dao.get_taxonomy_by_single_param(sql)
                        self.print_plant_info(self.get_full_plant_info_by_taxonomy(taxonomy_list))
                else:
                    print("输入有误")
            else:
                print("输入有误")
        else:
            print("输入错误")

    def cultivate(self):
        pass

    def maintain(self):
        pass

    def get_full_plant_info(self, plant_id):
        taxonomy_dao = TaxonomyDAOImpl()
        plant_image_dao = PlantImageDAOImpl()
        plant_dao = PlantDAOImpl()

        full_plant_info = FullPlantInfo()
        full_plant
