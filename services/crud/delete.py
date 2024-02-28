from fastapi import Request
from core.responses import Response_200


def delete_one(request: Request, collection_name: str, parameter: dict):
    request.app.database[collection_name].delete_one(parameter)
    return Response_200()(f"Record № {parameter} is deleted")
