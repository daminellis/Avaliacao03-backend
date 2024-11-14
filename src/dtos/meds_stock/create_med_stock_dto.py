from enums.meds_type import MedsType
from datetime import date

class CreateMedStockDTO:
    def __init__(self, med_name: str, med_qtd: int, med_val: date, med_desc: str, med_type: MedsType, user_id: int):
        self.med_name = med_name
        self.med_qtd = med_qtd
        self.med_val = med_val
        self.med_desc = med_desc
        self.med_type = med_type
        self.user_id = user_id