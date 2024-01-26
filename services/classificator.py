from fastapi import Request
from .crud.get import get_one, get_all
from .crud.create import create_one
from bson import ObjectId
from models.classificators import Classificators


collection_name = 'classificators'


def get_classificator(request: Request, id: str):
    return get_one(request, collection_name, {'_id': ObjectId(id)})


def create_classificator(request: Request, data: Classificators):
    return create_one(request, data, collection_name)


def get_all_classificators(request: Request):
    return get_all(request, collection_name)
