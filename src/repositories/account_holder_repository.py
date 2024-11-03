from mysqldb import db_connection
from models import AccountHolder


class AccountHolderRepository:
    def __init__(self):
        pass

    @staticmethod
    def find_account_holder_by_document(document):
        session = db_connection.db_session()
        account_holder = session.query(AccountHolder).filter(
            AccountHolder.document == document
        ).first()
        session.close()
        return account_holder

    @staticmethod
    def save_account_holder(account_holder):
        session = db_connection.db_session()
        session.add(AccountHolder(**account_holder))
        session.commit()
        session.close()

account_holder_repository = AccountHolderRepository()

