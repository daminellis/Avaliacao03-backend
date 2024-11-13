from typing import Optional
from dataclasses import dataclass

@dataclass
class SuccessDTO:
    code: int
    success: bool = True
    data: Optional[dict] = None