from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str
    preco_custo: float
    preco_venda: float
    quantidade: int = 0 

class ProdutoUpdate(BaseModel):
    nome: str
    preco_custo: float
    preco_venda: float