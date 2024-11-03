from datetime import datetime
from pydantic import BaseModel


class Transaction(BaseModel):
    wallet_id: str
    amount: float
    type: str
    timestamp: datetime

