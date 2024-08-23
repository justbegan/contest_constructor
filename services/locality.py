from fastapi import Request
from bson import ObjectId

from .crud.get import get_one_method


collection_name = "classificators"


def get_locality_by_settlement_id(request: Request, id: int):
    parameter = {
        "_id": ObjectId("66c8188278c3b5b05adb26e2"),
    }
    data = get_one_method(request, collection_name, parameter)

    index = {}
    for entry in data['data']:

        mun_id = entry["MunicID"]
        if mun_id not in index:
            index[mun_id] = []
        index[mun_id].append(entry)

    return index.get(id, [])


def get_locality_by_district_id(request: Request, distict_id: int):
    parameter = {
        "_id": ObjectId("66c8188278c3b5b05adb26e2"),
    }
    data = get_one_method(request, collection_name, parameter)

    index = {}
    for entry in data['data']:

        r_id = entry["RegID"]
        if r_id not in index:
            index[r_id] = []
        index[r_id].append(entry)

    return index.get(distict_id, [])
