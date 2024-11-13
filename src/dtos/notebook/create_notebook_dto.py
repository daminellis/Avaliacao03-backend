from enums.notebook import MedMethod, Status
from enums.meds_type  import MedsType
from datetime import datetime

class NotebookDTO:
    def __init__(self, note_title: str, med_stock_id: int, note_desc: str, med_method: MedMethod, med_type: MedsType, med_freq: str, qtd_taken: int, qtd_total: int, init_schedule: datetime, end_schedule: datetime, status: Status, obs: str, user_id: int):
        self.note_title = note_title
        self.med_stock_id = med_stock_id
        self.note_desc = note_desc
        self.med_method = med_method
        self.med_type = med_type
        self.med_freq = med_freq
        self.qtd_taken = qtd_taken
        self.qtd_total = qtd_total
        self.init_schedule = init_schedule
        self.end_schedule = end_schedule
        self.status = status
        self.obs = obs
        self.user_id = user_id