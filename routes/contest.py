from fastapi.routing import APIRouter
from services.contest import get_all_contests
from fastapi import Request


router = APIRouter(
    prefix='/contes',
    tags=['Конкурсы']
)


@router.get("/get_contests")
def get(request: Request):
    """
    Получить все конкурсы
    """
    return get_all_contests(request)
