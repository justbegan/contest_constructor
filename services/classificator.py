from fastapi import Request
from .crud.get import get_one
from bson import ObjectId


def get_classificator(request: Request, id: str):
    """
    Получить классификатор по id
    """
    collection_name = 'classificators'
    return get_one(request, collection_name, {'_id': ObjectId(id)})
