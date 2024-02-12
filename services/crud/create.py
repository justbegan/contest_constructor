from fastapi import Request
from core.responses import Response_200
from fastapi.encoders import jsonable_encoder


def create_one_method(request: Request, data: dict, collection_name: str):
    """
    Принимает request и создаваемый json
    \nВозвращает созданный объект
    """
    data = jsonable_encoder(data)
    insert = request.app.database[collection_name].insert_one(data)
    inserted_id = insert.inserted_id
    inserted_object = request.app.database[collection_name].find_one({"_id": inserted_id})
    inserted_object["_id"] = str(inserted_object["_id"])
    return inserted_object


def create_one(request: Request, data: dict, collection_name: str):
    """
    Принимает request и создаваемый json
    \nВозвращает созданный объект
    """
    inserted_object = create_one_method(request, data, collection_name)
    return Response_200()(inserted_object)
