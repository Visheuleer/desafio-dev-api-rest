from repositories import wallet_repository
from schemas import WalletSchema

class WalletServices:
    def __init__(self, id_account_holder):
        self._id_account_holder = id_account_holder


    def generate_wallet(self) -> WalletSchema:
        return WalletSchema(
        account_holder_id=self._id_account_holder,
        branch_code='0001',
        account_number=wallet_repository.generate_account_number(),
        balance=0.0,
        status=1,
        limit=2000
    )


    def model_to_schema(self, wallet) -> WalletSchema:
        return WalletSchema(
            account_holder_id=self._id_account_holder,
            branch_code=wallet.branch_code,
            account_number=wallet.account_number,
            balance=wallet.balance,
            status=wallet.status,
            limit=wallet.limit
        )



