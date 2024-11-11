from enum import Enum

class MedMethod(Enum):
    DIARIO = 'diário'
    CONTROLADO = 'controlado'

class Status(Enum):
    ATIVO = 'ativo'
    COMPLETO = 'completo'
    CANCELADO = 'cancelado'