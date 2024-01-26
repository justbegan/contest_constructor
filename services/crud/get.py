from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
import math
from core.responses import Response_500, Response_200
from fastapi.responses import JSONResponse


def get_all(request: Request, collection_name: str, parameter: dict = {}):
    """
    Получить все документы их коллекции
    """
    try:
        result = get_all_method(request, collection_name, parameter)
        return Response_200()(result)
    except RequestValidationError as e:
        return Response_500()(request, str(e))


def get_one(request: Request, collection_name: str, parameter: dict):
    """
    Получить один документ по id
    """
    try:
        data = get_one_method(request, collection_name, parameter)
        return Response_200()(data)
    except RequestValidationError as e:
        return Response_500()(request, str(e))


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
    PAGE_SIZE = page_size
    try:
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
    except RequestValidationError as e:
        return Response_500()(request, str(e))
