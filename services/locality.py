from fastapi import Request

from .crud.get import get_all, get_all_method


collection_name = "geo_locality"


def get_locality_by_settlement_id(request: Request, settlement_id: int):
    parameter = {"MunicID": settlement_id}
    return get_all(request, collection_name, parameter)


def get_locality_by_district_id(request: Request, distict_id: int):
    settlement = get_all_method(request, "geo_settlement", {"RegID": distict_id})
    settlement_ids = []
    for s in settlement:
        settlement_ids.append(s['MunicID'])
    parameter = {"MunicID": {"$in": settlement_ids}}
    return get_all(request, collection_name, parameter)
