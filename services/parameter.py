from fastapi import Request
from bson.objectid import ObjectId

from services.crud.create import create_one
from services.crud.get import get_all, get_one_method
from services.crud.delete import delete_one

from core.responses import Response_400


def create_parameter(request: Request, data: dict):
    collection_name = 'parameters'
    key = next(iter(data.keys()))
    duplicate = get_one_method(request, collection_name, {key: {"$exists": True}})
    if duplicate is None:
        return create_one(request, data, collection_name)
    else:
        return Response_400()(request, "parameter already exists")


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
        return Response_400()(request, str(e))
