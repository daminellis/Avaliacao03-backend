from typing import Optional

class UpdatePersonDTO:
    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None , age: Optional[int] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def set_last_name(self, last_name: str):
        self.last_name = last_name

    def set_age(self, age: int):
        self.age = age