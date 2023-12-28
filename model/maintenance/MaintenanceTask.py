from dataclasses import dataclass
from datetime import datetime

@dataclass
class MaintenanceTask:
    task_id: int = 0
    task_name: str = ""
    execution_time: str = ""
    location: str = ""
    personnel: str = ""
    description: str = ""
    plant_id: int = 0
    creator: str = ""
    create_time: datetime = None
    update_time: datetime = None

    def __post_init__(self):
        self.create_time = self.create_time if self.create_time is None else datetime.fromisoformat(self.create_time)
        self.update_time = self.update_time if self.update_time is None else datetime.fromisoformat(self.update_time)
