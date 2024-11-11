from enums.meds_type import MedsType

class MedsStockDTO:
    def __init__(self, meds_name: str, meds_qtd: int, meds_val: str, mds_desc: str, meds_type: MedsType, person_id: int):
        self.meds_name = meds_name
        self.meds_qtd = meds_qtd
        self.meds_val = meds_val
        self.mds_desc = mds_desc
        self.meds_type = meds_type
        self.person_id = person_id