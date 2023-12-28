from dataclasses import dataclass

@dataclass
class PlantImage:
    image_id: int = 0  # 图片编号
    plant_id: int = 0  # 植物编号
    location: str = ""  # 拍摄地点
    description: str = ""  # 描述
    photographer: str = ""  # 拍摄人
    photo_path: str = ""  # 图片路径
