from typing import List, Optional
from dataclasses import dataclass

@dataclass
class ErrorDTO:
    code: int
    message: str
    success: bool = False
    details: Optional[List[str]] = None