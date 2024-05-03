from fastapi.routing import APIRouter
from fastapi import Request
from services.statement import (
    create_statement, get_statements, get_statements_by_user,
    update_stamement, get_statements_by_id
)
from services.fields.current_user import get_current_profile
# from examples.statement import st_exam


router = APIRouter(
    prefix='/statement',
    tags=['Заявки']
)


@router.post("/create_statement")
def create(request: Request, data: dict, contest_oid: str = None):
    """
    Создать заявку
    """
    if contest_oid is None:
        profile = get_current_profile(request)
        contest_oid = profile['profile']['contest']
    return create_statement(request, contest_oid, data)


@router.post("/get_statements")
def get(request: Request, contest_oid: str = None,
        page: int = 1, page_size: int = 10, parameter: dict = {}):
    """
    Получить все заявки по oid конкурса
    """
    if contest_oid is None:
        profile = get_current_profile(request)
        contest_oid = profile['profile']['contest']
    return get_statements(request, contest_oid, page, page_size, parameter)


@router.get("/get_statements_by_user")
def get_by_user(request: Request, contest_oid: str = None, user_oid: str = '21412321321321'):
    """
    Получить все заявки по oid конкурса и user_oid
    """
    if contest_oid is None:
        profile = get_current_profile(request)
        contest_oid = profile['profile']['contest']
    return get_statements_by_user(request, contest_oid, user_oid)


@router.get("/get_statements_by_id")
def get_by_id(request: Request, contest_oid: str = None, statement_id: str = '21412321321321'):
    """
    Получить все заявки по oid конкурса и user_oid
    """
    if contest_oid is None:
        profile = get_current_profile(request)
        contest_oid = profile['profile']['contest']
    return get_statements_by_id(request, contest_oid, statement_id)


@router.put("/update_statement")
def update(request: Request, statement_oid: str, data: dict, contest_oid: str = None):
    """
    Обновить заявку по oid
    """
    if contest_oid is None:
        profile = get_current_profile(request)
        contest_oid = profile['profile']['contest']
    return update_stamement(request, statement_oid, data, contest_oid)
