from typing import Optional
from dataclasses import dataclass

@dataclass
class SuccessDTO:
    code: int
    message: Optional[str] = "Requisiçao realizada com sucesso"
    data: Optional[dict] = "Nenhum dado a ser retornado"
    success: bool = True