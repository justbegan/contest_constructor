from fastapi import Request
from .crud.get import get_all


def get_all_contests(request: Request):
    """
    Получить список всех конкурсов
    """
    table_name = 'contests'
    parameter = {"active": True}
    contests = get_all(request, table_name, parameter)
    return contests
