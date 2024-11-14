from typing import Optional
from enums.meds_type import MedsType

class UpdateMedStockDTO:
    def __init__(self, med_name: Optional[str] = None, med_qtd: Optional[int] = None, med_val: Optional[str] = None, med_desc: Optional[str] = None, med_type: Optional[MedsType] = None, user_id: Optional[int] = None):
        self.med_name = med_name
        self.med_qtd = med_qtd
        self.med_val = med_val
        self.med_desc = med_desc
        self.med_type = med_type
        self.user_id = user_id