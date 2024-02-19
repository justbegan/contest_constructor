from fastapi.routing import APIRouter
from services.comment import create_comment, get_all_comments_by_statement_oid
from fastapi import Request
from models.comments import Comments


router = APIRouter(
    prefix='/comment',
    tags=['Комментарий']
)


@router.get("/get_all")
def get(request: Request, statement_oid: str):
    """
    Получить все комментарии по oid заявки
    """
    return get_all_comments_by_statement_oid(request, statement_oid)


@router.post("/create")
def create(request: Request, data: Comments):
    """
    Создать комментарий
    """
    return create_comment(request, data)
