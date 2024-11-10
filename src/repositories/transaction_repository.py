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
    def find_transactions_by_wallet_id_period(wallet_id, start_date, end_date):
        session = db_connection.db_session()
        transactions = session.query(Transaction).filter(
            Transaction.wallet_id == wallet_id,
            Transaction.created_at >= start_date,
            Transaction.created_at <= end_date
        ).all()
        session.close()
        return transactions

    @staticmethod
    def save_transaction(transaction):
        session = db_connection.db_session()
        session.add(Transaction(**transaction))
        session.commit()
        session.close()

transaction_repository = TransactionRepository()


