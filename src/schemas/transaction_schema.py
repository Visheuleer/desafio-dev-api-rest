from datetime import datetime
from pydantic import BaseModel


class TransactionSchema(BaseModel):
    wallet_id: str
    amount: float
    created_at: datetime

