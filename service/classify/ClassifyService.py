
from datetime import datetime

from DAO.DAOFactory import DAOFactory
from model.classify.Distribution import Distribution
from model.classify.PlantClassify import PlantClassify
from model.classify.TaxonomyClassify import TaxonomyClassify





class ClassifyService:
    welcome = "欢迎来到 园林植物分类管理 模块"
    options = """
            1.增加植物分类信息
            2.删除植物分类信息
            3.修改植物分类信息
            4.查询植物分类信息
            5.根据科或属或种查询下属植物信息
            6.根据生长环境查询
            """

    @staticmethod
    def service():
        print(ClassifyService.welcome)
        print(ClassifyService.options)

        choice = int(input("请选择操作（输入数字）: "))

        if choice == 1:
            ClassifyService.add_classify_info()
        elif choice == 2:
            ClassifyService.delete_class_info()
        elif choice == 3:
            ClassifyService.update_class_info()
        elif choice == 4:
            ClassifyService.query_class_info()
        elif choice == 5:
            ClassifyService.query_by_taxonomy_name()
        elif choice == 6:
            ClassifyService.query_by_growth_environment()
        else:
            print("无效的选择！")

    @staticmethod
    def add_classify_info():
        scanner = input

        print("请输入植物分类信息：")
        plant_id = int(input("植物ID: "))

        plant_dao = DAOFactory.create_plant_dao()
        plant = plant_dao.get_plant_by_id(plant_id)

        if not plant:
            print("您输入的植物未找到。")
            return

        family_name = input("科名: ")
        genus_name = input("属名: ")
        species_name = input("种名: ")
        common_name = input("别名: ")
        growth_environment = input("生长环境: ")
        province_name = input("所在省: ")
        city_name = input("所在市: ")
        county_name = input("所在县: ")
        create_by = input("创建者: ")

        current_time = datetime.now()

        # Adding province
        distribution = Distribution()
        distribution.name = province_name
        distribution.level = "Province"
        distribution_dao = DAOFactory.get_distribution_dao()
        result1 = distribution_dao.add_distribution(distribution, False)

        if result1:
            print("植物分类省份信息添加成功!")
        else:
            print("植物分类信息省份添加失败。")

        # Adding city
        distribution1 = Distribution()
        distribution1.name = city_name
        distribution1.level = "City"
        distribution1.parent_distribution_id = distribution.distribution_id
        result2 = distribution_dao.add_distribution(distribution1, True)

        if result2:
            print("植物分类市信息添加成功!")
        else:
            print("植物分类市信息添加失败。")

        # Adding county
        distribution2 = Distribution()
        distribution2.name = county_name
        distribution2.level = "County"
        distribution2.parent_distribution_id = distribution1.distribution_id
        result3 = distribution_dao.add_distribution(distribution2, True)

        if result3:
            print("植物分类县信息添加成功!")
        else:
            print("植物分类县信息添加失败。")

        # Adding family name
        taxonomy_classify = TaxonomyClassify()
        taxonomy_classify.name = family_name
        taxonomy_classify.level = "Family"
        taxonomy_classify.parent_taxonomy_id = -1
        taxonomy_classify_dao = DAOFactory.get_taxonomy_calssify_dao()
        result4 = taxonomy_classify_dao.add_taxonomy_classify(taxonomy_classify, False)

        if result4:
            print("植物分类科名信息添加成功!")
        else:
            print("植物分类科名信息添加失败。")

        # Adding genus name
        taxonomy_classify1 = TaxonomyClassify()
        taxonomy_classify1.name = genus_name
        taxonomy_classify1.level = "Genus"
        taxonomy_classify1.parent_taxonomy_id = taxonomy_classify.taxonomy_id
        result5 = taxonomy_classify_dao.add_taxonomy_classify(taxonomy_classify1, True)

        if result5:
            print("植物分类属名信息添加成功!")
        else:
            print("植物分类属名信息添加失败。")

        # Adding species name
        taxonomy_classify2 = TaxonomyClassify()
        taxonomy_classify2.name = species_name
        taxonomy_classify2.level = "Species"
        taxonomy_classify2.parent_taxonomy_id = taxonomy_classify1.taxonomy_id
        result6 = taxonomy_classify_dao.add_taxonomy_classify(taxonomy_classify2, True)

        if result6:
            print("植物分类种名信息添加成功!")
        else:
            print("植物分类种名信息添加失败。")

        plant_classify = PlantClassify()
        plant_classify.plant_id = plant_id
        plant_classify.common_name = common_name
        plant_classify.growth_environment = growth_environment
        plant_classify.taxonomy_id = taxonomy_classify2.taxonomy_id
        plant_classify.distribution_id = distribution2.distribution_id
        plant_classify.create_by = create_by
        plant_classify.create_time = current_time

        plant_classify_dao = DAOFactory.get_plant_classify_dao()
        result = plant_classify_dao.add_plant_classify(plant_classify)

        if result:
            print("植物分类信息添加成功！")
        else:
            print("植物分类信息添加失败。")

    @staticmethod
    def delete_class_info():
        scanner = input

        print("请输入要删除植物的id")
        plant_id = int(input())

        plant_classify_dao = DAOFactory.get_plant_classify_dao()
        plant_classify = plant_classify_dao.get_plant_classify_by_id(plant_id)

        if plant_classify:
            tax = plant_classify.taxonomy_id
            dis = plant_classify.distribution_id

            result = plant_classify_dao.delete_plant_classify(plant_id)

            if result:
                print("已成功删除")
            else:
                print("删除失败")

            # Deleting taxonomy
            taxonomy_classify_dao = DAOFactory.get_taxonomy_calssify_dao()
            taxonomy_classify = taxonomy_classify_dao.get_taxonomy_classify_by_id(tax)
            taxonomy_classify1 = taxonomy_classify_dao.get_taxonomy_classify_by_id(taxonomy_classify.parent_taxonomy_id)
            result1 = taxonomy_classify_dao.delete_taxonomy_classify(tax)
            result2 = taxonomy_classify_dao.delete_taxonomy_classify(taxonomy_classify.parent_taxonomy_id)
            result3 = taxonomy_classify_dao.delete_taxonomy_classify(taxonomy_classify1.parent_taxonomy_id)

            if result1 and result2 and result3:
                print("科属种已成功删除")
            else:
                print("科属种删除失败")

            # Deleting province city county
            distribution_dao = DAOFactory.get_distribution_dao()
            distribution = distribution_dao.get_distribution_by_id(dis)
            distribution1 = distribution_dao.get_distribution_by_id(distribution.parent_distribution_id)
            distribution2 = distribution_dao.get_distribution_by_id(distribution1.parent_distribution_id)
            result4 = distribution_dao.delete_distribution(dis)
            result5 = distribution_dao.delete_distribution(distribution.parent_distribution_id)
            result6 = distribution_dao.delete_distribution(distribution1.parent_distribution_id)

            if result4 and result5 and result6:
                print("省市县已成功删除")
            else:
                print("省市县删除失败")
        else:
            print("植物分类信息未找到。")

    @staticmethod
    def update_class_info():
        scanner = input

        print("请输入需要更新的植物分类ID: ")
        plant_classify_id = int(input())
        plant_classify_dao = DAOFactory.get_plant_classify_dao()
        plant_classify = plant_classify_dao.get_plant_classify_by_id(plant_classify_id)

        if plant_classify:
            tax = plant_classify.taxonomy_id
            dis = plant_classify.distribution_id
            time = plant_classify.create_time

            family_name = input("科名: ")
            genus_name = input("属名: ")
            species_name = input("种名: ")
            common_name = input("别名: ")
            growth_environment = input("生长环境: ")
            province_name = input("所在省: ")
            city_name = input("所在市: ")
            county_name = input("所在县: ")
            updater = input("更新者: ")

            current_time = datetime.now()

            # Updating plant_classify
            plant_classify = PlantClassify()
            plant_classify.plant_id = plant_classify_id
            plant_classify.common_name = common_name
            plant_classify.growth_environment = growth_environment
            plant_classify.create_by = updater
            plant_classify.create_time = time
            plant_classify.taxonomy_id = tax
            plant_classify.distribution_id = dis
            plant_classify.update_time = current_time
            result = plant_classify_dao.update_plant_classify(plant_classify)

            if result:
                print("植物分类信息更新成功！")
            else:
                print("植物分类信息更新失败。")

            # Updating taxonomy
            taxonomy_classify_dao = DAOFactory.get_taxonomy_calssify_dao()
            taxonomy_classify = taxonomy_classify_dao.get_taxonomy_classify_by_id(tax)
            taxonomy_classify.name = species_name
            taxonomy_classify1 = taxonomy_classify_dao.get_taxonomy_classify_by_id(taxonomy_classify.parent_taxonomy_id)
            taxonomy_classify1.name = genus_name
            taxonomy_classify2 = taxonomy_classify_dao.get_taxonomy_classify_by_id(taxonomy_classify1.parent_taxonomy_id)
            taxonomy_classify2.name = family_name
            result1 = taxonomy_classify_dao.update_taxonomy_classify(taxonomy_classify)
            result2 = taxonomy_classify_dao.update_taxonomy_classify(taxonomy_classify1)
            result3 = taxonomy_classify_dao.update_taxonomy_classify(taxonomy_classify2)

            if result1 and result2 and result3:
                print("科属种已成功更新")
            else:
                print("科属种更新失败")

            # Updating province city county
            distribution_dao = DAOFactory.get_distribution_dao()
            distribution = distribution_dao.get_distribution_by_id(dis)
            distribution.name = county_name
            distribution1 = distribution_dao.get_distribution_by_id(distribution.parent_distribution_id)
            distribution1.name = city_name
            distribution2 = distribution_dao.get_distribution_by_id(distribution1.parent_distribution_id)
            distribution2.name = province_name
            result4 = distribution_dao.update_distribution(distribution)
            result5 = distribution_dao.update_distribution(distribution1)
            result6 = distribution_dao.update_distribution(distribution2)

            if result4 and result5 and result6:
                print("省市县已成功更新")
            else:
                print("省市县更新失败")
        else:
            print("植物分类信息未找到。")

    @staticmethod
    def query_class_info():

        print("输入要查询植物的id")
        plant_classify_id = int(input())

        plant_classify_dao = DAOFactory.get_plant_classify_dao()
        plant_classify = plant_classify_dao.get_plant_classify_by_id(plant_classify_id)

        taxonomy_classify_dao = DAOFactory.get_taxonomy_calssify_dao()
        print(plant_classify)
        taxonomy_classify = taxonomy_classify_dao.get_taxonomy_classify_by_id(plant_classify.taxonomy_id())
        taxonomy_classify1 = taxonomy_classify_dao.get_taxonomy_classify_by_id(taxonomy_classify.get_parent_taxonomy_id())
        taxonomy_classify2 = taxonomy_classify_dao.get_taxonomy_classify_by_id(taxonomy_classify1.get_parent_taxonomy_id())

        distribution_dao = DAOFactory.get_distribution_dao()
        distribution = distribution_dao.get_distribution_by_id(plant_classify.distribution_id())
        distribution1 = distribution_dao.get_distribution_by_id(distribution.get_parent_distribution_id())
        distribution2 = distribution_dao.get_distribution_by_id(distribution1.get_parent_distribution_id())

        print("科名：" + taxonomy_classify2.get_name())
        print("属名：" + taxonomy_classify1.get_name())
        print("种名：" + taxonomy_classify.get_name())
        print("别名：" + plant_classify.get_common_name())
        print("生长环境；" + plant_classify.get_growth_environment())
        print("所在省份：" + distribution2.get_name())
        print("所在市：" + distribution1.get_name())
        print("所在县：" + distribution.get_name())
        print("创建人员：" + plant_classify.get_creator())
        print("创建时间：" + plant_classify.get_create_time())
        print("更新时间：" + plant_classify.get_update_time())

    @staticmethod
    def query_by_growth_environment():

        print("输入要查询植物的生长环境")
        ge = input()

        plant_classify_dao = DAOFactory.get_plant_classify_dao()
        plant_classify_list = plant_classify_dao.query_by_growth_environment(ge)

        if plant_classify_list:
            for plant_classify in plant_classify_list:
                taxonomy_classify_dao = DAOFactory.get_taxonomy_calssify_dao()
                taxonomy_classify = taxonomy_classify_dao.get_taxonomy_classify_by_id(plant_classify.get_taxonomy_id())
                taxonomy_classify1 = taxonomy_classify_dao.get_taxonomy_classify_by_id(
                    taxonomy_classify.get_parent_taxonomy_id())
                taxonomy_classify2 = taxonomy_classify_dao.get_taxonomy_classify_by_id(
                    taxonomy_classify1.get_parent_taxonomy_id())

                distribution_dao = DAOFactory.get_distribution_dao()
                distribution = distribution_dao.get_distribution_by_id(plant_classify.get_distribution_id())
                distribution1 = distribution_dao.get_distribution_by_id(distribution.get_parent_distribution_id())
                distribution2 = distribution_dao.get_distribution_by_id(distribution1.get_parent_distribution_id())

                print("科名：" + taxonomy_classify2.get_name())
                print("属名：" + taxonomy_classify1.get_name())
                print("种名：" + taxonomy_classify.get_name())
                print("别名：" + plant_classify.get_common_name())
                print("生长环境；" + plant_classify.get_growth_environment())
                print("所在省份：" + distribution2.get_name())
                print("所在市：" + distribution1.get_name())
                print("所在县：" + distribution.get_name())
                print("创建人员：" + plant_classify.get_creator())
                print("创建时间：" + plant_classify.get_create_time())
                print("更新时间：" + plant_classify.get_update_time())
                print(" ------------------------------------")
        else:
            print("未检索到对应的植物信息")
    @staticmethod
    def query_by_taxonomy_name():

        print("输入要查询植物的科或属或种名")
        tn = input()

        plant_classify_dao = DAOFactory.get_plant_classify_dao()
        integer_list = plant_classify_dao.get_plant_ids_by_taxonomy(tn)

        if integer_list:
            for integer in integer_list:
                plant_classify = plant_classify_dao.get_plant_classify_by_id(integer)
                taxonomy_classify_dao = DAOFactory.get_taxonomy_calssify_dao()
                taxonomy_classify = taxonomy_classify_dao.get_taxonomy_classify_by_id(plant_classify.get_taxonomy_id())
                taxonomy_classify1 = taxonomy_classify_dao.get_taxonomy_classify_by_id(
                    taxonomy_classify.get_parent_taxonomy_id())
                taxonomy_classify2 = taxonomy_classify_dao.get_taxonomy_classify_by_id(
                    taxonomy_classify1.get_parent_taxonomy_id())

                distribution_dao = DAOFactory.get_distribution_dao()
                distribution = distribution_dao.get_distribution_by_id(plant_classify.get_distribution_id())
                distribution1 = distribution_dao.get_distribution_by_id(distribution.get_parent_distribution_id())
                distribution2 = distribution_dao.get_distribution_by_id(distribution1.get_parent_distribution_id())

                print("科名：" + taxonomy_classify2.get_name())
                print("属名：" + taxonomy_classify1.get_name())
                print("种名：" + taxonomy_classify.get_name())
                print("别名：" + plant_classify.get_common_name())
                print("生长环境；" + plant_classify.get_growth_environment())
                print("所在省份：" + distribution2.get_name())
                print("所在市：" + distribution1.get_name())
                print("所在县：" + distribution.get_name())
                print("创建人员：" + plant_classify.get_creator())
                print("创建时间：" + plant_classify.get_create_time())
                print("更新时间：" + plant_classify.get_update_time())
                print(" ------------------------------------")
        else:
            print("未检索到对应植物信息")


if __name__ == '__main__':
    # 测试
    ClassifyService.service()

