from fastapi import Request
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from core.responses import Response_400

from .crud.update import update_one
from .crud.create import create_one
from .crud.get import get_all, get_one_method, get_pagination
from bson.objectid import ObjectId
from datetime import datetime
import calendar


def get_statements(request: Request, contest_oid: str, page: int, page_size: int, parameter: dict = {}):
    """
    Получить все заявки по oid конкурса
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    return get_pagination(request, collection_name, page, page_size, parameter)


def get_statements_by_user(request: Request, contest_oid: str, user_oid: str):
    """
    Получить все заявки по oid конкурса и oid пользователя
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    return get_all(request, collection_name, {"user_oid": user_oid})


def create_statement(request: Request, contest_oid: str, data: dict):
    """
    Создает заявку
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    try:
        schema = get_schema_for_statement(request, contest_oid)
    except Exception as e:
        return Response_400()(request, str(e))
    try:
        data = {key: value for key, value in data.items() if key in schema.get("properties", {}) and value != ''}
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return Response_400()(request, e.message)
    current_date_time = datetime.utcnow()
    utc_time = calendar.timegm(current_date_time.utctimetuple())
    data['created_at'] = utc_time
    return create_one(request, data, collection_name)


def update_stamement(request: Request, statement_oid: str, data: dict, contest_oid: str):
    """
    Обновляет заявку
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    try:
        schema = get_schema_for_statement(request, contest_oid)
    except Exception as e:
        return Response_400()(request, str(e))
    try:
        data = {key: value for key, value in data.items() if key in schema.get("properties", {}) and value != ''}
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return Response_400()(request, str(e))
    parameter = {'_id': ObjectId(statement_oid)}
    return update_one(request, data, collection_name, parameter)


def get_schema_for_statement(request: Request, contest_oid: str):
    schema = get_one_method(request, 'schemas', {"contest_oid": contest_oid})
    return schema


def get_contest_collection_name(request: Request, contest_oid: str):
    contest = get_one_method(request, 'contests', {"_id": ObjectId(contest_oid)})
    return contest.get("unique_name")
