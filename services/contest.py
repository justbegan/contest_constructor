from fastapi import Request
from .crud.get import get_all
from .crud.create import create_one
from models.contest import Contests


def get_all_contests(request: Request):
    """
    Получить список всех конкурсов
    """
    table_name = 'contests'
    parameter = {"active": True}
    return get_all(request, table_name, parameter)


def create_contest(request: Request, data: Contests):
    """
    Создать конкурс
    """
    table_name = 'contests'
    return create_one(request, data, table_name)
