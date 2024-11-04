from sqlalchemy import Column, CHAR, String, Float, Integer,ForeignKey
from sqlalchemy.orm import relationship
from models import Base
import uuid

class WalletSequence(Base):
    __tablename__ = "wallet_sequence"
    id = Column(Integer, primary_key=True, autoincrement=True)


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    account_holder_id = Column(CHAR(36), ForeignKey("account_holders.id"), nullable=False, index=True)
    branch_code = Column(String(4), nullable=False, index=True)
    account_number = Column(String(8), autoincrement=True, nullable=False, unique=True, index=True)
    balance = Column(Float, nullable=False, index=True)
    status = Column(Integer, nullable=False, default=1, index=True)

    owner = relationship("AccountHolder", back_populates="wallet")
    transactions = relationship("Transaction", back_populates="wallet")