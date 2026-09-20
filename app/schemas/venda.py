from pydantic import BaseModel, Field

class ItemVendaCreate(BaseModel):
    produto_id: int
    quantidade: int = Field(gt=0)

class VendaCreate(BaseModel):
    itens: list[ItemVendaCreate] = Field(min_length=1)