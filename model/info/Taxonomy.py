from dataclasses import dataclass

@dataclass
class Taxonomy:
    taxonomy_id: int = 0  # 分类学编号
    family: str = ""  # 科名
    genus: str = ""  # 属名
    species: str = ""  # 种名
    plant_id: int = 0  # 植物编号
