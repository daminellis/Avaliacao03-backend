from typing import Optional

class UpdateUserDTO:
    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None , age: Optional[int] = None, password: Optional[str] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password