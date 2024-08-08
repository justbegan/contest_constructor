from fastapi import Request
from bson import ObjectId

from .crud.get import get_all_method, get_count, get_one
from .crud.create import create_one
from models.contest import Contests
from core.responses import Response_200


collection_name = 'contests'


def get_all_contests(request: Request):
    """
    Получить список всех конкурсов
    """
    result = []
    parameter = {"active": True}
    contests = get_all_method(request, collection_name, parameter)
    for i in contests:
        count = get_count(request, i['unique_name'])
        i['statements_count'] = count
        result.append(i)
    return Response_200()(result)


def create_contest(request: Request, data: Contests):
    """
    Создать конкурс
    """
    return create_one(request, data, collection_name)


def get_contest_by_id(request: Request, id: str):
    """
    Получить конкурс по id
    """
    return get_one(request, collection_name, {"_id": ObjectId(id)})
