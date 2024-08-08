from fastapi.routing import APIRouter
from services.contest import get_all_contests, create_contest, get_contest_by_id
from fastapi import Request
from models.contest import Contests


router = APIRouter(
    prefix='/contest',
    tags=['Конкурсы']
)


@router.get("/get_contests")
def get(request: Request):
    """
    Получить все конкурсы
    """
    return get_all_contests(request)


@router.get("/get_contest_by_id")
def get_by_id(request: Request, id: str):
    """
    Получить по id
    """
    return get_contest_by_id(request, id)


@router.post("/create_contest")
def create(request: Request, data: Contests):
    """
    Создать конкуос
    """
    return create_contest(request, data)
