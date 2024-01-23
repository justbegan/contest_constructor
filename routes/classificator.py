from fastapi.routing import APIRouter
from services.classificator import get_classificator
from fastapi import Request


router = APIRouter(
    prefix='/classificator',
    tags=['Классификаторы']
)


@router.get("/get_classificator")
def get(request: Request, id: str):
    """
    Получить классификатор по oid
    """
    return get_classificator(request, id)
