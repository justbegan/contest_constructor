from fastapi.routing import APIRouter
from fastapi import Request

from services.news import get_all_news, get_news_by_id, create_news, update_news, delete_news
from models.news import News


router = APIRouter(
    prefix='/news',
    tags=['Новости']
)


@router.get("/get_news")
def get(request: Request):
    """
    Получить все новости
    """
    return get_all_news(request)


@router.get("/get_by_id")
def get_by_id(request: Request, oid: str):
    """Получить по id"""
    return get_news_by_id(request, oid)


@router.post("/create_news")
def create(request: Request, data: News):
    """
    Создать новость
    """
    return create_news(request, data)


@router.put("/update_news")
def update(request: Request, data: News, news_oid: str):
    """
    Обновить новость
    """
    return update_news(request, data, news_oid)


@router.delete("/delete_news")
def delete(request: Request, news_oid: str):
    """
    Удалить новость
    """
    return delete_news(request, news_oid)
