# classify_service.py
from DAO.classify.FamilyDAO import FamilyDAO
from DAO.classify.GenusDAO import GenusDAO
from DAO.classify.SpeciesDAO import SpeciesDAO


class ClassifyService:
    def __init__(self):
        self.family_dao = FamilyDAO()
        self.genus_dao = GenusDAO()
        self.species_dao = SpeciesDAO()

    def add_family(self):
        family_name = input("请输入科名：")
        self.family_dao.add_family(family_name)
        print("科信息添加成功。")

    def modify_family_info(self):
        family_id = input("请输入要修改的科的ID：")
        #检查是否存在
        if self.family_dao.get_family_by_id(family_id) is None:
            print("科不存在。")
            return
        new_family_name = input("请输入新的科名：")
        self.family_dao.update_family(family_id, new_family_name)
        print("科信息修改成功。")

    def delete_family(self):
        family_id = input("请输入要删除的科的ID：")
        #检查是否存在
        if self.family_dao.get_family_by_id(family_id) is None:
            print("科不存在。")
            return
        #检查是否有下属分类
        if self.genus_dao.get_genera_by_family_id(family_id) is not None:
            print("科下有属，不能删除。")
            return
        self.family_dao.delete_family(family_id)
        print("科信息删除成功。")

    def get_all_families(self):
        families = self.family_dao.get_all_families()
        print("科列表：")
        for family in families:
            print(f"ID: {family.family_id}, 科名: {family.family_name}")
        print("按任意键返回")
        input()

    def show_classification_tree(self):
        # 科属种树形分类目录
        tree={}
        families=self.family_dao.get_all_families()
        print("科/属/种")
        for family in families:
            print(f"{family.family_name}")
            genera=self.genus_dao.get_genera_by_family_id(family.family_id)
            for genus in genera:
                print(f"   {genus.genus_name}")
                species=self.species_dao.get_species_by_genus_id(genus.genus_id)

                for specie in species:
                    print(f"     {specie.species_name}")


    def get_all_genera(self):
        genera = self.genus_dao.get_all_genera()
        print("属列表：")
        for genus in genera:
            print(f"ID: {genus.genus_id}, 属名: {genus.genus_name}")
        input("按任意键返回")

    def modify_genus_info(self):
        genus_id = input("请输入要修改的属的ID：")
        #检查是否存在
        if self.genus_dao.get_genus_by_id(genus_id) is None:
            print("属不存在。")
            return
        new_genus_name = input("请输入新的属名：")
        self.genus_dao.update_genus(genus_id, new_genus_name)
        print("属信息修改成功。")

    def add_genus(self):
        genus_name = input("请输入属名：")
        family_id = input("请输入所属科的ID：")
        #检查科是否存在
        if self.family_dao.get_family_by_id(family_id) is None:
            print("科不存在。")
            return
        self.genus_dao.add_genus(genus_name, family_id)
        print("属信息添加成功。")

    def delete_genus(self):
        genus_id = input("请输入要删除的属的ID：")
        #检查是否存在
        if self.genus_dao.get_genus_by_id(genus_id) is None:
            print("属不存在。")
            return
        #检查是否有下属分类
        if self.species_dao.get_species_by_genus_id(genus_id) is not None:
            print("属下有种，不能删除。")
            return
        self.genus_dao.delete_genus(genus_id)
        print("属信息删除成功。")

    def get_all_species(self):
        species_vos = self.species_dao.get_all_species_view()
        self.print_specis_vo(species_vos)

    def modify_species_info(self):
        species_id = input("请输入要修改的种的ID：")
        #检查是否存在
        speice=self.species_dao.get_species_by_id(species_id)
        if speice is None:
            print("种不存在。")
            return

        new_species_name = input("请输入新的种名(按回车键跳过)：")
        new_species_name=new_species_name if new_species_name!='' else speice.species_name
        new_species_alias = input("请输入新的种别名(按回车键跳过)：")
        new_species_alias=new_species_alias if new_species_alias!='' else speice.species_alias
        new_species_genus_id = input("请输入新的属ID(按回车键跳过)：")
        new_species_genus_id=new_species_genus_id if new_species_genus_id!='' else speice.genus_id
        #检查属是否存在
        if self.genus_dao.get_genus_by_id(new_species_genus_id) is None:
            print("属不存在。")
            return
        new_species_growth_env=input("请输入新的生长环境(按回车键跳过)：")
        new_species_growth_env=new_species_growth_env if new_species_growth_env!='' else speice.growth_env
        new_species_province=input("请输入新的省份(按回车键跳过)：")
        new_species_province=new_species_province if new_species_province!='' else speice.province
        new_species_city=input("请输入新的城市(按回车键跳过)：")
        new_species_city=new_species_city if new_species_city!='' else speice.city
        new_species_country=input("请输入新的县(按回车键跳过)：")
        new_species_country=new_species_country if new_species_country!='' else speice.country
        self.species_dao.update_species(species_id, new_species_name,new_species_alias,new_species_genus_id,new_species_growth_env,new_species_province,new_species_city,new_species_country)
        print("种信息修改成功。")

    def add_species(self):
        species_name = input("请输入种名：")
        genus_id = input("请输入所属属的ID：")
        #检查属是否存在
        if self.genus_dao.get_genus_by_id(genus_id) is None:
            print("属不存在。")
            return
        self.species_dao.add_species(species_name, genus_id)
        print("种信息添加成功。")

    def delete_species(self):
        species_id = input("请输入要删除的种的ID：")
        #检查是否存在
        if self.species_dao.get_species_by_id(species_id) is None:
            print("种不存在。")
            return
        self.species_dao.delete_species(species_id)
        print("种信息删除成功。")

    def search_by_environment(self):
        growth_env = input("请输入生长环境：")
        species_vos = self.species_dao.get_species_view_by_growth_env(growth_env)
        self.print_specis_vo(species_vos)

    def search_by_family(self):
        family_name = input("请输入科名：")
        species_vos = self.species_dao.get_species_view_by_family(family_name)
        self.print_specis_vo(species_vos)

    def search_by_genus(self):
        genus_name = input("请输入属名：")
        species_vos = self.species_dao.get_species_view_by_genus(genus_name)
        self.print_specis_vo(species_vos)

    def print_specis_vo(self,species_vos):
        print("ID  种名  种别名  属名  科名  生长环境  省  市  县")
        for specie_vo in species_vos:
            # 宽度对齐
            # print(f"{specie_vo.species_id} {specie_vo.species_name} {specie_vo.species_alias} {specie_vo.genus_name} {specie_vo.family_name} {specie_vo.growth_env} {specie_vo.province} {specie_vo.city} {specie_vo.country}")
            print(
                f"{specie_vo.species_id:<5} {specie_vo.species_name:<10} {specie_vo.species_alias:<10} {specie_vo.genus_name:<10} {specie_vo.family_name:<10} {specie_vo.growth_env:<10} {specie_vo.province:<10} {specie_vo.city:<10} {specie_vo.country:<10}")
        input("按任意键返回")




if __name__ == '__main__':
    classify_service = ClassifyService()
    classify_service.show_classification_tree()
    pass