from pydantic import BaseModel


class WalletSchema(BaseModel):
    account_holder_id: str
    branch_code: str
    account_number: str
    balance: float
    status: int
    limit: float

