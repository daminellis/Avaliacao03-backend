from enums.notebook import MedMethod, Status
from enums.meds_type  import MedsType
from datetime import datetime

class NotebookDTO:
    def __init__(self, title: str, med_name: str, description: str, method: MedMethod, med_type: MedsType, med_freq: str, qtd_taken: int, qtd_total: int, init_schedule: datetime, end_schedule: datetime, status: Status, obs: str, person_id: int):
        self.title = title
        self.med_name = med_name
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