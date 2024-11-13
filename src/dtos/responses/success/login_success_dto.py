from dataclasses import dataclass

@dataclass
class LoginSuccessDTO:
    code: int
    access_token: str
    success: bool = True