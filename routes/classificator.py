from fastapi.routing import APIRouter
from fastapi import Request
from services.classificator import (get_classificator, create_classificator, get_all_classificators)
from models.classificators import Classificators


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


@router.get("/get_all_classificators")
def get_all(request: Request):
    """
    Получить все классификаторы
    """
    return get_all_classificators(request)


@router.post("/create_classsificator")
def post(request: Request, data: Classificators):
    """
    Создать классификатор
    """
    return create_classificator(request, data)
