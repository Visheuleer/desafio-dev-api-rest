from sqlalchemy import Column, CHAR, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base
import datetime
import uuid

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    wallet_id = Column(CHAR(36), ForeignKey("wallets.id"), nullable=False)

    wallet = relationship("Wallet", back_populates="transactions")
