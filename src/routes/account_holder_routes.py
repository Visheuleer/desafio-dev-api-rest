from fastapi import APIRouter, HTTPException, status
from repositories import account_holder_repository, wallet_repository
from schemas import AccountHolderSchema
from services import AccountHolderServices


router = APIRouter(prefix='/account-holder', tags=['Account Holder'])


@router.get('/{document}', status_code=status.HTTP_200_OK)
def get_account_holder(document: str):
    account_holder = account_holder_repository.find_account_holder_by_document(document)
    if not account_holder:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'CPF: "{document}" não encontrado.')
    return account_holder


@router.post('/register', status_code=status.HTTP_201_CREATED)
def register_account_holder(account_holder: AccountHolderSchema):
    if account_holder_repository.find_account_holder_by_document(account_holder.document):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'CPF "{account_holder.document}" já cadastrado.')
    if not AccountHolderServices(account_holder.document).document_is_valid():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'CPF "{account_holder.document}" inválido.')
    account_holder_repository.save_account_holder(account_holder.dict())
    return account_holder


@router.delete('/{document}', status_code=status.HTTP_204_NO_CONTENT)
def delete_account_holder(document: str):
    account_holder_id = account_holder_repository.get_account_holder_id_by_document(document)
    if account_holder_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'CPF: "{document}" não encontrado.')
    wallet_repository.delete_wallet(account_holder_id)
    account_holder_repository.delete_account_holder(document)
    return None