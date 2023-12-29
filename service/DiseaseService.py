from DAO.pestcontrol.DseaseDAO import DiseaseDAO


class DiseaseService():
    def __init__(self):
        self.disease_dao = DiseaseDAO()

    def get_all(self):
        ds=self.disease_dao.get_all_diseases()
        print("ID 病虫害名称  防治方法  药剂  用量  时间")
        for d in ds:
            print(f"{d.disease_id} {d.disease_name} {d.method} {d.drug} {d.dosage} {d.time}")
        input("按回车键继续")

    def add(self):
        disease_name = input("请输入病虫害名称：")
        if disease_name == '':
            print("病虫害名称不能为空")
            return

        method = input("请输入防治方法：")
        drug = input("请输入药剂：")
        dosage = input("请输入用量：")
        time = input("请输入作用时间：")
        self.disease_dao.add_disease(disease_name, method, drug, dosage, time)
        print("添加成功")
        pass

    def update(self):
        disease_id = input("请输入病虫害ID：")
        # 检验ID是否存在
        disease=self.disease_dao.get_disease_by_id(disease_id)
        if disease is None:
            print("病虫害ID不存在")
            return

        disease_name = input("请输入病虫害名称(按回车键跳过)：")
        disease_name = disease_name if disease_name != '' else disease.disease_name
        method=input("请输入防治方法(按回车键跳过)：")
        method = method if method != '' else disease.method
        drug=input("请输入药剂(按回车键跳过)：")
        drug = drug if drug != '' else disease.drug
        dosage=input("请输入用量(按回车键跳过)：")
        dosage = dosage if dosage != '' else disease.dosage
        time=input("请输入作用时间(按回车键跳过)：")
        time = time if time != '' else disease.time
        self.disease_dao.update_disease(disease_id, disease_name, method, drug, dosage, time)
        print("修改成功")

    def delete(self):
        disease_id = input("请输入病虫害ID：")
        # 检验ID是否存在
        disease=self.disease_dao.get_disease_by_id(disease_id)
        if disease is None:
            print("病虫害ID不存在")
            return
        self.disease_dao.delete_disease(disease_id)
        print("删除成功")
        pass




