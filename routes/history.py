from fastapi.routing import APIRouter
from fastapi import Request

from services.history import get_history_by_st_oid


router = APIRouter(
    prefix='/history',
    tags=['История']
)


@router.get("/get_parameters")
def get(request: Request, statement_oid: str):
    """
    Получить историю заявки по oid Заявки
    """
    return get_history_by_st_oid(request, statement_oid)
