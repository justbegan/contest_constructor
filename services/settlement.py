from fastapi import Request
from bson import ObjectId

from .crud.get import get_one_method


collection_name = "classificators"


def get_settlement_by_ra_id(request: Request, id: int):
    parameter = {
        "_id": ObjectId("66c7e76d78c3b5b05adb26d8"),
    }
    data = get_one_method(request, collection_name, parameter)
    index = {}
    for entry in data['data']:
        reg_id = entry["RegID"]
        if reg_id not in index:
            index[reg_id] = []
        index[reg_id].append(entry)

    return index.get(id, [])
