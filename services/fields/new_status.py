from services.crud.get import get_one_method
from fastapi import Request
from bson import ObjectId


def new_status(request: Request, contest_oid: str) -> dict:
    """
    При создании заявки подставляет 1 статус
    как правило это статус 'Создана'
    """
    try:
        schema = get_one_method(request, "schemas", {"contest_oid": contest_oid})
        classificator = schema['properties']['status']['properties']['class']['classifficator_id']
        status = get_one_method(request, 'classificators', {"_id": ObjectId(classificator)})['data'][0]
        return {
            "class": classificator,
            "value": status['id']
        }
    except:
        raise Exception("Can't got new status from db")
