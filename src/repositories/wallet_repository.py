from sqlalchemy.dialects.mysql import insert
from mysqldb import db_connection
from models import Wallet, WalletSequence


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
    def generate_account_number():
        session = db_connection.db_session()
        result = session.execute(insert(WalletSequence).values())
        session.commit()
        session.close()
        return f"{result.inserted_primary_key[0]:08}"

    @staticmethod
    def save_wallet(wallet):
        session = db_connection.db_session()
        session.add(Wallet(**wallet))
        session.commit()
        session.close()

    @staticmethod
    def delete_wallet(account_holder_id):
        session = db_connection.db_session()
        wallet = session.query(Wallet).filter(
            Wallet.account_holder_id == account_holder_id
        ).first()
        if wallet is not None:
            session.delete(wallet)
            session.commit()
        session.close()

wallet_repository = WalletRepository()

