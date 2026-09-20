from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime
from app.database import Base

class Venda(Base):
    __tablename__ = "vendas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    data_hora = Column(
        DateTime,
        default=datetime.now,
        nullable=False
    )

    valor_total = Column(
        Float,
        nullable=False
    )