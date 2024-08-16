from fastapi.routing import APIRouter
from fastapi import Request

from services.settlement import get_settlement_by_ra_id

router = APIRouter(
    prefix='/settlement',
    tags=['Поселения']
)


@router.get("/get_settlements")
def get(request: Request, reg_id: int):
    """
    Получить поселения по id района
    """
    return get_settlement_by_ra_id(request, reg_id)
