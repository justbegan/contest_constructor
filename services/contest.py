from fastapi import Request
from .crud.get import get_all_method, get_count
from .crud.create import create_one
from models.contest import Contests
from core.responses import Response_200, Response_500


collection_name = 'contests'


def get_all_contests(request: Request):
    """
    Получить список всех конкурсов
    """
    try:
        result = []
        parameter = {"active": True}
        contests = get_all_method(request, collection_name, parameter)
        for i in contests:
            count = get_count(request, i['unique_name'])
            i['statements_count'] = count
            result.append(i)
        return Response_200()(result)
    except Exception as e:
        return Response_500()(request, str(e))


def create_contest(request: Request, data: Contests):
    """
    Создать конкурс
    """
    return create_one(request, data, collection_name)
