from fastapi import Request

from models.schema import Schemas
from fastapi.encoders import jsonable_encoder
from .crud.create import create_one
from .crud.update import update_one
from .crud.get import get_all, get_one, get_one_method

from core.responses import Response_400
from bson import ObjectId

collection_name = 'schemas'


def create_schema(request: Request, data: Schemas):
    """
    Создает схему
    """
    data = jsonable_encoder(data)
    if 'user_oid' not in data['properties']:
        return Response_400()(request, "user_oid not found")
    if 'user_oid' not in data['required']:
        return Response_400()(request, "user_oid user_oid must be mandatory")
    contest_oid = data.get('contest_oid', None)
    if contest_oid is None:
        return Response_400()(request, "contest_oid required paramether")
    if get_one_method(request, 'schemas', {"contest_oid": contest_oid}) is None:
        return create_one(request, data, collection_name)
    else:
        return Response_400()(request, "selected contest already has a schema")


def update_schema(request: Request, id: str, data: Schemas):
    """
    Создает схему
    """
    data = jsonable_encoder(data)
    if 'user_oid' not in data['properties']:
        return Response_400()(request, "user_oid not found")
    if 'user_oid' not in data['required']:
        return Response_400()(request, "user_oid user_oid must be mandatory")
    contest_oid = data.get('contest_oid', None)
    if contest_oid is None:
        return Response_400()(request, "contest_oid required paramether")
    if get_one_method(request, 'schemas', {"contest_oid": contest_oid}) is not None:
        parameter = {'_id': ObjectId(id)}
        return update_one(request, data, collection_name, parameter)
    else:
        return Response_400()(request, "schema not found")


def get_schema_by_contest_id(request: Request, contest_oid: str):
    """
    Получить схему по id конкурса
    """
    try:
        return get_one(request, 'schemas', {"contest_oid": contest_oid})
    except Exception as e:
        return Response_400()(request, str(e))


def get_schema_by_id(request: Request, id: str):
    parameter = {'_id': ObjectId(id)}
    return get_one(request, collection_name, parameter)


def get_all_schemas(request: Request):
    try:
        return get_all(request, collection_name)
    except Exception as e:
        return Response_400()(request, str(e))
