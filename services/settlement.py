from fastapi import Request

from .crud.get import get_all


collection_name = "geo_settlement"


def get_settlement_by_ra_id(request: Request, reg_id: int):
    parameter = {"RegID": reg_id}
    return get_all(request, collection_name, parameter)
