from sqlalchemy.dialects.mysql import insert
from models import WalletSequence
from repositories import wallet_repository
from schemas import WalletSchema
from mysqldb import db_connection

class WalletServices:
    def __init__(self, id_account_holder):
        self._id_account_holder = id_account_holder


    def generate_wallet(self):
        return WalletSchema(
        account_holder_id=self._id_account_holder,
        branch_code='0001',
        account_number=wallet_repository.generate_account_number(),
        balance=0.0,
        status=1
    )




