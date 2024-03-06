from fastapi import Request
from .crud.get import get_all_method
from .crud.create import create_one
from .fields.current_user import get_current_user, get_profile_by_user_id
from models.comments import Comments


collection_name = 'comments'


def get_all_comments_by_statement_oid(request: Request, statement_oid: str):
    """
    Получить список всех
    """
    parameter = {"statement_oid": statement_oid}
    comments = get_all_method(request, collection_name, parameter)
    return add_user_name(request, comments)


def create_comment(request: Request, data: Comments):
    """
    Создать комментарий
    """

    data.author = get_current_user(request)
    return create_one(request, data, collection_name)


def add_user_name(request: Request, comments: list):
    for c in comments:
        try:
            c['author_name'] = get_profile_by_user_id(request, c['author'])['username']
        except:
            c['author_name'] = None
    return comments
