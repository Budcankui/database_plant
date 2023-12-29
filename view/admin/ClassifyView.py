# classify_view.py
from service.ClassifyService import ClassifyService


class ClassifyView:
    def __init__(self, user):
        self.user = user
        self.classify_service = ClassifyService()

    def start(self):
        while True:
            print("欢迎使用植物分类管理系统。")
            print("1. 科管理")
            print("2. 属管理")
            print("3. 物种信息管理")
            print("4. 查看科属种分类树")
            print("5. 退出")

            choice = input("请输入选项：")

            if choice == '1':
                self.manage_family()
            elif choice == '2':
                self.manage_genus()
            elif choice == '3':
                self.manage_species()
            elif choice == '4':
                self.show_classification_tree()
            elif choice == '5':
                print("退出植物分类管理系统。")
                break
            else:
                print("无效选项，请重新输入。")

    def manage_family(self):
        print("1. 查看科名:")
        print("2. 修改科名")
        print("3. 添加科名")
        print("4. 删除科名")
        choice = input("请输入选项：")
        if choice == '1':
            self.view_family_list()
        elif choice == '2':
            self.modify_family_info()
        elif choice == '3':
            self.add_family()
        elif choice == '4':
            self.delete_family()
        else:
            print("无效选项，请重新输入。")

    def add_family(self):
        self.classify_service.add_family()

    def modify_family_info(self):
        self.classify_service.modify_family_info()

    def delete_family(self):
        self.classify_service.delete_family()

    def view_family_list(self):
        self.classify_service.get_all_families()


    def show_classification_tree(self):
        self.classify_service.show_classification_tree()
        pass

    def manage_genus(self):
        print("1. 查看属名:")
        print("2. 修改属名")
        print("3. 添加属名")
        print("4. 删除属名")
        choice = input("请输入选项：")
        if choice == '1':
            self.view_genus_list()
        elif choice == '2':
            self.modify_genus_info()
        elif choice == '3':
            self.add_genus()
        elif choice == '4':
            self.delete_genus()
        else:
            print("无效选项，请重新输入。")

    def view_genus_list(self):
        self.classify_service.get_all_genera()

    def modify_genus_info(self):
        self.classify_service.modify_genus_info()

    def add_genus(self):
        self.classify_service.add_genus()

    def delete_genus(self):
        self.classify_service.delete_genus()

    def manage_species(self):
        print("1. 查询物种信息:")
        print("2. 修改物种信息")
        print("3. 添加物种信息")
        print("4. 删除物种信息")
        print("5. 根据生长环境模糊查询")
        print("6. 根据科查询下属植物")
        print("7. 根据属名查询下属植物")
        choice = input("请输入选项：")
        if choice == '1':
            self.view_species_list()
        elif choice == '2':
            self.modify_species_info()
        elif choice == '3':
            self.add_species()
        elif choice == '4':
            self.delete_species()
        elif choice == '5':
            self.classify_service.search_by_environment()
        elif choice == '6':
            self.classify_service.search_by_family()
        elif choice == '7':
            self.classify_service.search_by_genus()
        else:
            print("无效选项，请重新输入。")

    def view_species_list(self):
        self.classify_service.get_all_species()

    def modify_species_info(self):
        self.classify_service.modify_species_info()

    def add_species(self):
        self.classify_service.add_species()

    def delete_species(self):
        self.classify_service.delete_species()


if __name__ == '__main__':
    ClassifyView('admin').start()