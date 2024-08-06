from fastapi import Request
from fastapi.encoders import jsonable_encoder
import math
from core.responses import Response_200
from fastapi.responses import JSONResponse
from services.fields.current_user import get_current_profile


def get_all(request: Request, collection_name: str, parameter: dict = {}):
    """
    Получить все документы их коллекции
    """
    result = get_all_method(request, collection_name, parameter)
    return Response_200()(result)


def get_one(request: Request, collection_name: str, parameter: dict):
    """
    Получить один документ по id
    """
    data = get_one_method(request, collection_name, parameter)
    return Response_200()(data)


def get_one_method(request: Request, collection_name: str, parameter: dict):
    """
    Базовый метод, получение отдного объекта
    """
    data = request.app.database[collection_name].find_one(parameter)
    try:
        data["_id"] = str(data["_id"])
        result = jsonable_encoder(data)
        return result
    except:
        return None


def get_all_method(request: Request, collection_name: str, parameter: dict = {}):
    """
    Получить все документы их коллекции
    """
    try:
        data = request.app.database[collection_name].find(parameter)
        result = []
        for i in data:
            i["_id"] = str(i["_id"])
            result.append(i)
        return jsonable_encoder(result)
    except:
        return None


def get_pagination(request: Request, collection_name: str, page: int, page_size: int, parameter: dict = {}):
    """
    Получить пагинацию
    """
    user_proflie = get_current_profile(request).get("profile")
    parameter['user_oid'] = str(user_proflie.get("user"))
    if user_proflie.get("role_name") in ["admin", "moder"]:
        parameter.pop("user_oid")
    PAGE_SIZE = page_size
    skip = page * PAGE_SIZE - PAGE_SIZE
    collection_size = request.app.database[collection_name].count_documents(parameter)
    pages_count = math.ceil(collection_size / PAGE_SIZE)
    data = request.app.database[collection_name].find(parameter).skip(skip).limit(PAGE_SIZE)
    result = []
    for i in data:
        i["_id"] = str(i["_id"])
        result.append(i)
    result = jsonable_encoder(result)
    return JSONResponse(
        {
            "status": True,
            "data": result,
            "page": page,
            "pages_count": pages_count
        }
    )


def get_count(request: Request, collection_name: str, parameter: dict = {}):
    """
    Количество
    """
    try:
        data = request.app.database[collection_name].count_documents(parameter)
        return data
    except:
        return 0
