from enums.notebook import MedMethod, Status
from enums.meds_type import MedsType
from datetime import datetime
from typing import Optional

class UpdateNotebookDTO:
    def __init__(self, note_title: Optional[str], med_stock_id: Optional[int], note_desc:Optional[str], med_method: Optional[MedMethod], med_type: Optional[MedsType], med_freq: Optional[str], qtd_taken: Optional[int], qtd_total: Optional[int], init_schedule: Optional[datetime], end_schedule: Optional[datetime], status: Optional[Status], obs: Optional[str], user_id: Optional[int]):
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