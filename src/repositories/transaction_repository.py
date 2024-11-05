from mysqldb import db_connection
from models import Transaction


class TransactionRepository:
    def __init__(self):
        pass


    @staticmethod
    def find_transaction_by_id(transaction_id):
        session = db_connection.db_session()
        transaction = session.query(Transaction).filter(
            Transaction.id == transaction_id
        ).first()
        session.close()
        return transaction

    @staticmethod
    def save_transaction(transaction):
        session = db_connection.db_session()
        session.add(Transaction(**transaction))
        session.commit()
        session.close()

transaction_repository = TransactionRepository()


