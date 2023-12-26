from dataclasses import dataclass

@dataclass
class User:
    user_id: int = 0
    username: str = ""
    password: str = ""
    user_type: str = ""
