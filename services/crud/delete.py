from fastapi import Request
from core.responses import Response_500, Response_200


def delete_one(request: Request, collection_name: str, parameter: dict):
    try:
        delete = request.app.database[collection_name].delete_one(parameter)
        return Response_200()(delete)

    except Exception as e:
        return Response_500()(request, str(e))
