from fastapi import Request
from fastapi.responses import JSONResponse
from .get import get_one_method


def update_one(request: Request, data: dict, collection_name: str, parameter: dict):
    data = {"$set": data}
    request.app.database[collection_name].update_one(parameter, data)
    updated_object = get_one_method(request, collection_name, parameter)
    result = {
        "status": True,
        "data": updated_object
    }
    return JSONResponse(result)


def delete_created_at(data: dict) -> dict:
    obj = data.copy()
    del obj['created_at']
    return obj
