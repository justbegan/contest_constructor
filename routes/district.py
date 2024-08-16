from fastapi.routing import APIRouter
from fastapi import Request

from services.district import get_all_districts

router = APIRouter(
    prefix='/district',
    tags=['Районы']
)


@router.get("/get_districts")
def get(request: Request):
    """
    Получить историю заявки по oid Заявки
    """
    return get_all_districts(request)
