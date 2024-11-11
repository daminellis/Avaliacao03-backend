from enums.notebook import MedMethod, Status
from enums.meds_type import MedsType
from datetime import datetime
from typing import Optional

class UpdateNotebookDTO:
    def __init__(self, title: Optional[str] = None, note_name: Optional[str] = None, description: Optional[str] = None, method: Optional[MedMethod] = None, med_type: Optional[MedsType] = None, med_freq: Optional[str] = None, qtd_taken: Optional[int] = None, qtd_total: Optional[int] = None, init_schedule: Optional[datetime] = None, end_schedule: Optional[datetime] = None, status: Optional[Status] = None, obs: Optional[str] = None, person_id: Optional[int] = None):
        self.title = title
        self.note_name = note_name
        self.description = description
        self.method = method
        self.med_type = med_type
        self.med_freq = med_freq
        self.qtd_taken = qtd_taken
        self.qtd_total = qtd_total
        self.init_schedule = init_schedule
        self.end_schedule = end_schedule
        self.status = status
        self.obs = obs
        self.person_id = person_id