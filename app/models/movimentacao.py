from sqlalchemy import Column,Integer, String , ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base

class MovimentacaoEstoque(Base):
    __tablename__ = "movimentacoes_estoque"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    produto_id = Column(
        Integer,
        ForeignKey("produtos.id"),
        nullable=False
    )

    tipo = Column(
        String,
        nullable=False
    )

    quantidade = Column(
        String,
        nullable=False
    )

    motivo = Column(
        String,
        nullable=False
    )

    produto = relationship(
        "Produto",
        back_populates="movimentacoes"
    )

    data_hora = Column(
        DateTime,
        default=datetime.now,
        nullable=False
    )
