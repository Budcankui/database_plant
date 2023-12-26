from dataclasses import dataclass
from datetime import datetime

@dataclass
class PestControl:
    pest_control_id: int = 0
    pest_name: str = ""
    control_method: str = ""
    pesticide_name: str = ""
    pesticide_amount: str = ""
    effective_duration: str = ""
    creator: str = ""
    create_time: datetime = None
    update_time: datetime = None

    def __post_init__(self):
        self.create_time = self.create_time if self.create_time is None else datetime.fromisoformat(self.create_time)
        self.update_time = self.update_time if self.update_time is None else datetime.fromisoformat(self.update_time)
