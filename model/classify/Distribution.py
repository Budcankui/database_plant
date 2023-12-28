from dataclasses import dataclass

@dataclass
class Distribution:
    distribution_id: int
    parent_id: int  # 使用 int 以支持 null 值
    name: str
    level: str  # "Province", "City", "County"


