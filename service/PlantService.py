from DAO.info.PlantDAO import PlantDAO


class PlantService():
    def __init__(self):
        self.plant_dao = PlantDAO()

    def query_plant_list(self):
        plants = self.plant_dao.get_all_plants()
        print("ID 物种ID  病虫害ID  形态特征  应用价值  栽培要点  图片文件路径  配图描述  拍摄地点  配图描述  配图拍摄人  创建时间  更新时间")
        for plant in plants:
            print(plant.plant_id, plant.species_id, plant.disease_id, plant.plant_desc,
                  plant.plant_value, plant.plant_tip, plant.image_path, plant.image_desc,
                  plant.image_location, plant.create_by,
                  plant.create_time, plant.update_time)
        input("按回车键返回")

    def add_plant(self, user):
        specie_id = input("请输入物种ID：")
        # 检查物种ID是否存在
        specie = self.plant_dao.get_plant_by_id(specie_id)
        if specie is None:
            print("物种ID不存在")
            return
        disease_id = input("请输入病虫害ID(按回车跳过)：")
        # #检查病虫害ID是否存在
        # disease=self.plant_dao.get_plant_by_id(disease_id)
        # if disease is None:
        plant_desc = input("请输入形态特征(按回车跳过)：")
        plant_value = input("请输入应用价值(按回车跳过)：")
        plant_tip = input("请输入栽培要点(按回车跳过)：")
        image_path = input("请输入图片文件路径(按回车跳过)：")
        image_desc = input("请输入配图描述(按回车跳过)：")
        image_location = input("请输入拍摄地点(按回车跳过)：")
        create_by = user.user_id
        self.plant_dao.add_plant(specie_id, disease_id, plant_desc, plant_value,
                                 plant_tip, image_path, image_desc, image_location, create_by)

    def update_plant(self, user):
        plant_id = input("请输入要修改的植物ID：")
        plant = self.plant_dao.get_plant_by_id(plant_id)
        if plant is None:
            print("植物ID不存在")
            return
        specie_id = input("请输新的入物种ID(按回车跳过)：")
        specie_id = plant.species_id if specie_id == "" else specie_id
        # 检查物种ID是否存在
        specie = self.plant_dao.get_plant_by_id(specie_id)
        if specie is None:
            print("物种ID不存在")
            return
        disease_id = input("请输入新的病虫害ID(按回车跳过)：")
        disease_id = plant.disease_id if disease_id == "" else disease_id
        # #检查病虫害ID是否存在
        # disease=self.plant_dao.get_plant_by_id(disease_id)

        plant_desc = input("请输入新的形态特征(按回车跳过)：")
        plant_desc = plant.plant_desc if plant_desc == "" else plant_desc
        plant_value = input("请输入新的应用价值(按回车跳过)：")
        plant_value = plant.plant_value if plant_value == "" else plant_value
        plant_tip = input("请输入新的栽培要点(按回车跳过)：")
        plant_tip = plant.plant_tip if plant_tip == "" else plant_tip
        image_path = input("请输入新的图片文件路径(按回车跳过)：")
        image_path = plant.image_path if image_path == "" else image_path
        image_desc = input("请输入新的配图描述(按回车跳过)：")
        image_desc = plant.image_desc if image_desc == "" else image_desc
        image_location = input("请输入新的拍摄地点(按回车跳过)：")
        image_location = plant.image_location if image_location == "" else image_location
        create_by = user.user_id
        new_vlaues = {"species_id": specie_id, "disease_id": disease_id,
                      "plant_desc": plant_desc, "plant_value": plant_value,
                      "plant_tip": plant_tip, "image_path": image_path,
                      "image_desc": image_desc, "image_location": image_location,
                      "create_by": create_by}
        self.plant_dao.update_plant(plant_id, new_vlaues)

    def delete_plant(self):
        plant_id = input("请输入要删除的植物ID：")
        plant = self.plant_dao.get_plant_by_id(plant_id)
        if plant is None:
            print("植物ID不存在")
            return
        self.plant_dao.delete_plant(plant_id)
        print("删除成功")

    def query_plant_detail_view(self):
        plant_vos = self.plant_dao.query_plant_detail_view()
        print("ID  科  属  种  病名  防治方法  形态特征  应用价值  栽培要点  图片文件路径  配图描述  拍摄地点")
        for plant_vo in plant_vos:
            print(
                f"{plant_vo.plant_id}  {plant_vo.family_name}  "
                f"{plant_vo.genus_name}  {plant_vo.species_name}  "
                f"{plant_vo.disease_name}  {plant_vo.disease_control_method}"
                f"  {plant_vo.plant_desc}  {plant_vo.plant_value}  "
                f"{plant_vo.plant_tip}  {plant_vo.image_path}  "
                f"{plant_vo.image_desc}  {plant_vo.image_location}")

        input("按回车键返回")

    def query_plant_count_by_family(self):
        result = self.plant_dao.query_plant_count_by_family()
        print("科  数量")
        for family_name, count in result:
            print(f"{family_name}  {count}")
        input("按回车键返回")

    def query_plant_by_attribute(self):
        # 过滤条件的字典
        filter_conditions = {}
        print("请输入要查询的过滤条件(AND)：")
        family_name = input("科(按回车键跳过)：")
        if family_name != "":
            filter_conditions["family_name"] = family_name
        genus_name = input("属(按回车键跳过)：")
        if genus_name != "":
            filter_conditions["genus_name"] = genus_name
        species_name = input("种(按回车键跳过)：")
        if species_name != "":
            filter_conditions["species_name"] = species_name
        disease_name = input("病名(按回车键跳过)：")
        if disease_name != "":
            filter_conditions["disease_name"] = disease_name
        disease_control_method = input("防治方法(按回车键跳过)：")
        if disease_control_method != "":
            filter_conditions["disease_control_method"] = disease_control_method
        plant_desc = input("形态特征(按回车键跳过)：")
        if plant_desc != "":
            filter_conditions["plant_desc"] = plant_desc
        plant_value = input("应用价值(按回车键跳过)：")
        if plant_value != "":
            filter_conditions["plant_value"] = plant_value
        plant_tip = input("栽培要点(按回车键跳过)：")
        if plant_tip != "":
            filter_conditions["plant_tip"] = plant_tip
        image_desc = input("配图描述(按回车键跳过)：")
        if image_desc != "":
            filter_conditions["image_desc"] = image_desc
        image_location = input("拍摄地点(按回车键跳过)：")
        if image_location != "":
            filter_conditions["image_location"] = image_location
        # 查询结果
        plant_vos = self.plant_dao.query_plant_by_like_attribute(filter_conditions)
        print("ID  科  属  种  病名  防治方法  形态特征  应用价值  栽培要点  图片文件路径  配图描述  拍摄地点")
        for plant_vo in plant_vos:
            print(
                f"{plant_vo.plant_id}  {plant_vo.family_name}  "
                f"{plant_vo.genus_name}  {plant_vo.species_name}  "
                f"{plant_vo.disease_name}  {plant_vo.disease_control_method}"
                f"  {plant_vo.plant_desc}  {plant_vo.plant_value}  "
                f"{plant_vo.plant_tip}  {plant_vo.image_path}  "
                f"{plant_vo.image_desc}  {plant_vo.image_location}")
        input("按回车键返回")


