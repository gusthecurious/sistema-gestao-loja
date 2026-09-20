from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome = Column(
        String,
        nullable=False
    )

    preco_custo = Column(
        Float,
        nullable=False
    )

    preco_venda = Column(
        Float,
        nullable=False
    )

    quantidade = Column(
        Integer,
        default=0
    )

    movimentacoes = relationship(
        "MovimentacaoEstoque",
        back_populates="produto"
    )



