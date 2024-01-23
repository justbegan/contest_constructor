from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
# from bson.objectid import ObjectId


def get_all(request: Request, collection_name: str, parameter: dict = {}):
    """
    Получить все документы их коллекции
    """
    try:
        data = request.app.database[collection_name].find(parameter)
        result = []
        for i in data:
            i["_id"] = str(i["_id"])
            result.append(i)
        result = jsonable_encoder(result)
        return JSONResponse(
            {
                "status": True,
                "data": result
            }
        )
    except RequestValidationError as e:
        return JSONResponse(
            {
                "status": False,
                "data": str(e)
            }, status_code=500
        )


def get_one(request: Request, collection_name: str, parameter: dict):
    """
    Получить один документ по id
    """
    try:
        data = get_one_method(request, collection_name, parameter)
        return JSONResponse(
            {
                "status": True,
                "data": data
            }
        )
    except RequestValidationError as e:
        return JSONResponse(
            {
                "status": False,
                "data": str(e)
            }, status_code=500
        )


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
