from datetime import datetime
from pydantic import BaseModel


class TransactionSchema(BaseModel):
    wallet_id: str
    amount: float
    timestamp: datetime

