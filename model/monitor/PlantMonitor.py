from dataclasses import dataclass
from datetime import datetime

@dataclass
class PlantMonitor:
    id: int = 0
    monitoring_time: datetime = None
    monitoring_personnel: str = ""
    monitoring_location: str = ""
    monitored_object: str = ""
    monitored_object_id: int = 0
    monitor_value: float = 0.0
    monitoring_index: str = ""
    monitoring_device: str = ""
    created_by: str = ""
    created_time: datetime = None
    updated_time: datetime = None

    def __post_init__(self):
        self.monitoring_time = self.monitoring_time if self.monitoring_time is None else datetime.fromisoformat(self.monitoring_time)
        self.created_time = self.created_time if self.created_time is None else datetime.fromisoformat(self.created_time)
        self.updated_time = self.updated_time if self.updated_time is None else datetime.fromisoformat(self.updated_time)
