from fastapi.routing import APIRouter
from services.contest import get_all_contests, create_contest
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


@router.post("/create_contest")
def create(request: Request, data: Contests):
    """
    Создать конкуос
    """
    return create_contest(request, data)
