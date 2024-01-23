from fastapi import Request
from fastapi.responses import JSONResponse


def delete_one(request: Request, collection_name: str, parameter: dict):
    try:
        delete = request.app.database[collection_name].delete_one(parameter)
        result = {
            "status": True,
            "data": str(delete)
        }
        return JSONResponse(result)

    except Exception as e:
        return JSONResponse(
            {
                "status": False,
                "data": str(e)
            }, status_code=500
        )
