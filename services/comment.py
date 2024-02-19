from fastapi import Request
from .crud.get import get_all
from .crud.create import create_one
from .fields.current_user import get_current_user
from .fields.utctime import get_current_utc_time


collection_name = 'comments'


def get_all_comments_by_statement_oid(request: Request, statement_oid: str):
    """
    Получить список всех конкурсов
    """
    parameter = {"statment_oid": statement_oid}
    return get_all(request, collection_name, parameter)


def create_comment(request: Request, data: dict):
    """
    Создать комментарий
    """
    data['author'] = get_current_user(request)
    data['created_at'] = get_current_utc_time()
    return create_one(request, data, collection_name)
