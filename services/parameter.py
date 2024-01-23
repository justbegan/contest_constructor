from fastapi import Request

from services.crud.create import create_one
from services.crud.get import get_all, get_one_method
from services.crud.delete import delete_one
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId


def create_parameter(request: Request, data: dict):
    collection_name = 'parameters'
    key = next(iter(data.keys()))
    duplicate = get_one_method(request, collection_name, {key: {"$exists": True}})
    if duplicate is None:
        return create_one(request, data, collection_name)
    else:
        return JSONResponse({
            "status": False,
            "data": "parameter already exists"
        }, status_code=400)


def get_parameters(request: Request):
    collection_name = 'parameters'
    return get_all(request, collection_name)


def delete_parameter_by_oid(request: Request, schema_oid: str):
    """
    Получить схему по id конкурса
    """
    collection_name = 'parameters'
    try:
        parameter = {"_id": ObjectId(schema_oid)}
        schema = delete_one(request, collection_name, parameter)
        return schema
    except Exception as e:
        return JSONResponse(
            {
                "status": False,
                "data": str(e)
            }, status_code=400
        )
