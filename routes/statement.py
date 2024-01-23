from fastapi.routing import APIRouter
from fastapi import Request
from services.statement import (
    create_statement, get_statements, get_statements_by_user,
    update_stamement,
)
from examples.statement import st_exam


router = APIRouter(
    prefix='/statement',
    tags=['Заявки']
)


@router.post("/create_statement")
def create(request: Request, contest_oid: str = '65a767c72e0fe1554e0d3c9a', data: dict = st_exam):
    """
    Создать заявку
    """
    return create_statement(request, contest_oid, data)


@router.get("/get_statements")
def get(request: Request, contest_oid: str = '65a767c72e0fe1554e0d3c9a'):
    """
    Получить все заявки по oid конкурса
    """
    return get_statements(request, contest_oid)


@router.get("/get_statements_by_user")
def get_by_user(request: Request, contest_oid: str = '65a767c72e0fe1554e0d3c9a', user_oid: str = '21412321321321'):
    """
    Получить все заявки по oid конкурса и user_oid
    """
    return get_statements_by_user(request, contest_oid, user_oid)


@router.put("/update_statement")
def update(request: Request, statement_oid: str, data: dict, contest_oid: str):
    """
    Обновить заявку по oid
    """
    return update_stamement(request, statement_oid, data, contest_oid)
