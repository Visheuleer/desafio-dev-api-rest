from pydantic import BaseModel


class AccountHolderSchema(BaseModel):
    name: str
    document: str

