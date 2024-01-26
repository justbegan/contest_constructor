from fastapi.routing import APIRouter
from fastapi import Request
from services.schema import create_schema, get_schema_by_contest_id
from models.schema import Schemas

router = APIRouter(
    prefix='/schema',
    tags=['Схемы']
)


@router.post("/create_schema")
def create(request: Request, data: Schemas):
    """
    Создать схему
    """
    return create_schema(request, data)


@router.get("/get_schema")
def get(request: Request, contest_oid: str = '65a767c72e0fe1554e0d3c9a'):
    """
    Получить схему по oid конкурса
    """
    return get_schema_by_contest_id(request, contest_oid)
