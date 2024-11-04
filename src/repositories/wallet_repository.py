from mysqldb import db_connection
from models import Wallet


class WalletRepository:
    def __init__(self):
        pass

    @staticmethod
    def find_account_holder_by_account_holder_id(account_holder_id):
        session = db_connection.db_session()
        wallet = session.query(Wallet).filter(
            Wallet.account_holder_id == account_holder_id
        ).first()
        session.close()
        return wallet

    @staticmethod
    def save_wallet(wallet):
        session = db_connection.db_session()
        session.add(Wallet(**wallet))
        session.commit()
        session.close()

wallet_repository = WalletRepository()

