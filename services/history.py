import calendar
from datetime import datetime
from fastapi.requests import Request

from .crud.create import create_one_method
from .crud.get import get_all
from .fields.current_user import get_current_profile

collection_name = 'history'


def create_history(request: Request, statement_oid: str, text: str):
    current_date_time = datetime.utcnow()
    utc_time = calendar.timegm(current_date_time.utctimetuple())

    obj = {
        "statement_oid": statement_oid,
        "created_at": utc_time,
        "text": text,
        "author_name": get_current_profile(request)['username']
    }
    return create_one_method(request, obj, collection_name)


def get_history_by_st_oid(request: Request, obj_id: str):
    parameter = {"statement_oid": obj_id}
    return get_all(request, collection_name, parameter)
