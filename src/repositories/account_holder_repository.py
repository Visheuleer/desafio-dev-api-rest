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
    def get_account_holder_id_by_document(document):
        session = db_connection.db_session()
        account_holder = session.query(AccountHolder).filter(
            AccountHolder.document == document
        ).first()
        session.close()
        if account_holder is None:
            return None
        return account_holder.id

    @staticmethod
    def save_account_holder(account_holder):
        session = db_connection.db_session()
        session.add(AccountHolder(**account_holder))
        session.commit()
        session.close()

    @staticmethod
    def delete_account_holder(document):
        session = db_connection.db_session()
        account_holder = session.query(AccountHolder).filter(
            AccountHolder.document == document
        ).first()
        session.delete(account_holder)
        session.commit()
        session.close()
        return True

account_holder_repository = AccountHolderRepository()

