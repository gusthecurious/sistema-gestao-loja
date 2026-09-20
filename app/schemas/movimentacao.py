from pydantic import BaseModel,Field
from enum import Enum

class TipoMovimentacao(str, Enum):
    entrada = "entrada"
    saida = "saida"


class MovimentacaoCreate(BaseModel):
    produto_id: int
    tipo: TipoMovimentacao
    quantidade: int = Field(gt=0)
    motivo: str = Field(min_length=1)
    
