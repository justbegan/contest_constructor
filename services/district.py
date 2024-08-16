from fastapi import Request

from .crud.get import get_all


collection_name = "geo_district"


def get_all_districts(request: Request):
    return get_all(request, collection_name)
