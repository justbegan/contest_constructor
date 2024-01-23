from fastapi import Request
from fastapi.encoders import jsonable_encoder
from .crud.create import create_one
from .crud.get import get_all, get_one
from fastapi.responses import JSONResponse
from models.schema import Schemas


def create_schema(request: Request, data: Schemas):
    """
    Создает схему
    """
    collection_name = 'schemas'
    data = jsonable_encoder(data)
    if 'user_oid' not in data['properties']:
        return JSONResponse(
            {
                "status": False,
                "data": "user_oid not found"
            }, status_code=400
        )
    if 'user_oid' not in data['required']:
        return JSONResponse(
            {
                "status": False,
                "data": "user_oid user_oid must be mandatory"
            }, status_code=400
        )

    return create_one(request, data, collection_name)


def get_schema(request: Request):
    """
    Получить все схемы
    """
    collection_name = 'schemas'
    return get_all(request, collection_name)


def get_schema_by_contest_id(request: Request, contest_oid: str):
    """
    Получить схему по id конкурса
    """
    try:
        schema = get_one(request, 'schemas', {"contest_oid": contest_oid})
        return schema
    except Exception as e:
        return JSONResponse(
            {
                "status": False,
                "data": str(e)
            }, status_code=400
        )
