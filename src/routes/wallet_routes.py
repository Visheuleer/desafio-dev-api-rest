from fastapi import APIRouter, HTTPException, status
from repositories import wallet_repository, account_holder_repository
from schemas import WalletSchema
from services import WalletServices


router = APIRouter(prefix='/wallet', tags=['Wallet'])


@router.get('/{account_holder_id}', status_code=status.HTTP_200_OK)
def get_wallet(account_holder_id: str):
    wallet = wallet_repository.find_account_holder_by_account_holder_id(account_holder_id)
    if not wallet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Conta não encontrada.')
    return wallet


@router.post('/register/{document}', status_code=status.HTTP_201_CREATED)
def register_wallet(document: str):
    id_account_holder = account_holder_repository.get_account_holder_id_by_document(document)
    if id_account_holder is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'CPF "{document}" não cadastrado. Cadastre o CPF em: "/account-holder/register" antes de criar a conta.')
    if wallet_repository.find_account_holder_by_account_holder_id(id_account_holder):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'CPF "{document}" já tem uma conta.')

    wallet = WalletServices(id_account_holder).generate_wallet()
    wallet_repository.save_wallet(wallet.dict())
    return wallet
