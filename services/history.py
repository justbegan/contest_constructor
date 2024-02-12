from .crud.create import create_one_method
import calendar
from datetime import datetime
from fastapi.requests import Request

collection_name = 'history'


def create_history(request: Request, obj_id: str, text: str):
    try:
        current_date_time = datetime.utcnow()
        utc_time = calendar.timegm(current_date_time.utctimetuple())

        obj = {
            "obj_id": obj_id,
            "created_at": utc_time,
            "text": text
        }
        return create_one_method(request, obj, collection_name)
    except Exception as e:
        raise Exception(e)
