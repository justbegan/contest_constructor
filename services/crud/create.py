from fastapi import Request
from fastapi.responses import JSONResponse


def create_one(request: Request, data: dict, collection_name: str):
    """
    Принимает request и создаваемый json
    \nВозвращает созданный объект
    """
    try:
        insert = request.app.database[collection_name].insert_one(data)
        inserted_id = insert.inserted_id
        inserted_object = request.app.database[collection_name].find_one({"_id": inserted_id})
        inserted_object["_id"] = str(inserted_object["_id"])
        result = {
            "status": True,
            "data": inserted_object
        }
        return JSONResponse(result)

    except Exception as e:
        return JSONResponse(
            {
                "status": False,
                "data": str(e)
            }, status_code=500
        )
