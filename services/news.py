from fastapi import Request
from bson import ObjectId

from .crud.get import get_all
from .crud.create import create_one
from .crud.update import update_one
from .crud.delete import delete_one
from models.news import News
from services.fields.utctime import get_current_utc_time
from services.fields.current_user import get_current_profile
from core.responses import Response_400

collection_name = 'news'


def get_all_news(request: Request):
    """
    Получить список всех конкурсов
    """
    parameter = {"contest_oid": get_current_profile(request, 'contest')}
    return get_all(request, collection_name, parameter)


def create_news(request: Request, data: News):
    """
    Создать новость
    """
    obj = data.dict()
    obj['contest'] = get_current_profile(request, 'contest')
    obj['created_at'] = get_current_utc_time()
    obj['updated_at'] = get_current_utc_time()
    return create_one(request, obj, collection_name)


def update_news(request: Request, data: News, news_oid: str):
    """
    Обновление новостей
    """
    try:
        obj = data.dict()
        obj['updated_at'] = get_current_utc_time()
        parameter = {'_id': ObjectId(news_oid)}
        return update_one(request, obj, collection_name, parameter)
    except Exception as e:
        return Response_400()(request, str(e))


def delete_news(request: Request, news_oid: str):
    """
    Удалить новость
    """
    try:
        parameter = {"_id": ObjectId(news_oid)}
        obj = delete_one(request, collection_name, parameter)
        return obj
    except Exception as e:
        return Response_400()(request, str(e))
