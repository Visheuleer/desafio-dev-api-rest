from enums import WalletStatus

class TransactionServices:
    def __init__(self, wallet):
        self.wallet = wallet


    def is_wallet_active_unblocked(self):
        return self.wallet.status == WalletStatus.ACTIVE.value


    def is_wallet_limit_available(self, debit):
        return self.wallet.limit > debit


    def is_wallet_balance_sufficient(self, debit):
        return self.wallet.balance > debit


    def deposit_value(self, amount):
        self.wallet.balance += amount
        return self.wallet


    def debit_value(self, amount):
        self.wallet.balance -= amount
        return self.wallet


    def debit_limit(self, amount):
        self.wallet.limit -= amount