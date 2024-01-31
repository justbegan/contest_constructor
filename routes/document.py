from fastapi.routing import APIRouter
from services.document import get_all_documents
from fastapi import Request


router = APIRouter(
    prefix='/docs',
    tags=['Документы']
)


@router.get("/get_all_documents")
def get(request: Request):
    """
    Получить все документы
    """
    return get_all_documents(request)
