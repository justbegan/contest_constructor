from fastapi.routing import APIRouter
from fastapi import Request

from services.locality import get_locality_by_settlement_id, get_locality_by_district_id

router = APIRouter(
    prefix='/locality',
    tags=['Населенный пункт']
)


@router.get("/get_locality")
def get(request: Request, settlement_id: int):
    """
    Получить населенные пункты по id населения
    """
    return get_locality_by_settlement_id(request, settlement_id)


@router.get("/get_locality_by_district_id")
def get_by_distict(request: Request, district_id: int):
    """
    Получить населенные пункты по id населения
    """
    return get_locality_by_district_id(request, district_id)
