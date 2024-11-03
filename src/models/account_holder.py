from sqlalchemy import Column, CHAR, String
from sqlalchemy.orm import relationship
from models import Base
import uuid


class AccountHolder(Base):
    __tablename__ = "account_holders"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(255), nullable=False, index=True)
    document = Column(String(11), nullable=False, unique=True, index=True)

    wallet = relationship("Wallet", back_populates="owner", uselist=False)