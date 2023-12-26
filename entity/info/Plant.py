from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Plant:
    plant_id: int = 0  # 植物编号
    disease_name: str = ""  # 病名
    common_name: str = ""  # 别名
    morphology: str = ""  # 形态特征
    cultivation_tips: str = ""  # 栽培技术要点
    pest_control_measures: str = ""  # 病虫害防治措施
    application_value: str = ""  # 应用价值
    creator: str = ""  # 创建者
    create_time: datetime = None
    update_time: datetime =None

    def __post_init__(self):
        self.create_time = (
            self.create_time
            if self.create_time is None
            else datetime.fromtimestamp(self.create_time / 1000)
        )
        self.update_time = (
            self.update_time
            if self.update_time is None
            else datetime.fromtimestamp(self.update_time / 1000)
        )



