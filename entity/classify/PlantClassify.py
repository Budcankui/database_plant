from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class PlantClassify:
    plant_id: int
    common_name: str
    growth_environment: str
    taxonomy_id: int
    distribution_id: int
    creator: str
    create_time: datetime
    update_time: datetime