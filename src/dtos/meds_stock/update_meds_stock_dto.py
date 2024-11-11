from typing import Optional
from enums.meds_type import MedsType

class UpdateMedsStockDTO:
    def __init__(self, meds_name: Optional[str] = None, meds_qtd: Optional[int] = None, meds_val: Optional[str] = None, mds_desc: Optional[str] = None, meds_type: Optional[MedsType] = None, person_id: Optional[int] = None):
        self.meds_name = meds_name
        self.meds_qtd = meds_qtd
        self.meds_val = meds_val
        self.mds_desc = mds_desc
        self.meds_type = meds_type
        self.person_id = person_id