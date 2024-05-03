from fastapi.routing import APIRouter
from fastapi import Request
from services.schema import (create_schema, update_schema, get_schema_by_contest_id, get_all_schemas,
                             get_schema_by_id)
from models.schema import Schemas
from services.fields.current_user import get_current_profile

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


@router.put("/update_schema")
def update(request: Request, id: str, data: Schemas):
    """
    Создать схему
    """
    return update_schema(request, id, data)


@router.get("/get_schema")
def get(request: Request, contest_oid: str = None):
    """
    Получить схему по oid конкурса
    """
    if contest_oid is None:
        profile = get_current_profile(request)
        contest_oid = profile['profile']['contest']
    return get_schema_by_contest_id(request, contest_oid)


@router.get("/get_schema_by_id")
def get_by_id(request: Request, id: str):
    """
    Получить схему по id
    """
    return get_schema_by_id(request, id)


@router.get("/get_all")
def get_all(request: Request):
    """
    Получить все схемы
    """
    return get_all_schemas(request)
