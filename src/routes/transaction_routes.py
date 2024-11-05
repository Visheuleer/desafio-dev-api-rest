from fastapi import APIRouter, HTTPException, status
from schemas import TransactionSchema
from enums import TransactionType
from repositories import wallet_repository, transaction_repository
from services import TransactionServices, WalletServices


router = APIRouter(prefix='/transaction', tags=['Transaction'])


@router.get('/transaction', status_code=status.HTTP_200_OK)
def get_transaction(transaction_id):
    transaction = transaction_repository.find_transaction_by_id(transaction_id)
    if transaction is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Transação não encontrada.')
    return transaction


@router.post('/deposit', status_code=status.HTTP_201_CREATED)
def deposit(transaction: TransactionSchema):
    wallet = wallet_repository.find_wallet_by_id(transaction.wallet_id)
    if wallet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Conta não encontrada.')
    transaction_services = TransactionServices(wallet)
    if not transaction_services.is_wallet_active_unblocked():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Conta inativa ou bloqueada.')

    wallet = transaction_services.deposit_value(transaction.amount)
    wallet_repository.update_wallet(WalletServices(wallet.account_holder_id).model_to_schema(wallet).dict())
    transaction = transaction.dict()
    transaction['type'] = TransactionType.DEPOSIT.value
    transaction_repository.save_transaction(transaction)
    transaction['type'] = 'Depósito'
    return transaction


@router.post('/withdrawal', status_code=status.HTTP_201_CREATED)
def withdrawal(transaction: TransactionSchema):
    wallet = wallet_repository.find_wallet_by_id(transaction.wallet_id)
    if wallet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Conta não encontrada.')
    transaction_services = TransactionServices(wallet)
    if not transaction_services.is_wallet_active_unblocked():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Conta inativa ou bloqueada.')
    if not transaction_services.is_wallet_balance_sufficient(transaction.amount):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Saldo insuficiente.')
    if not transaction_services.is_wallet_limit_available(transaction.amount):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Limite diário atingido.')
    transaction_services.debit_limit(transaction.amount)
    wallet = transaction_services.debit_value(transaction.amount)
    wallet_repository.update_wallet(WalletServices(wallet.account_holder_id).model_to_schema(wallet).dict())
    transaction = transaction.dict()
    transaction['type'] = TransactionType.WITHDRAWAL.value
    transaction_repository.save_transaction(transaction)
    transaction['type'] = 'Saque'
    return transaction
