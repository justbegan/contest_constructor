from fastapi import Request
from bson import ObjectId

from .crud.get import get_all


def get_all_districts(request: Request):
    return get_all(request, "classificators", {"_id": ObjectId("66c2bd96aa9a95bb68fd6af5")})
