from fastapi import Request
from bson import ObjectId

from .crud.get import get_all
from .crud.create import create_one
from .crud.update import update_one
from .fields.utctime import get_current_utc_time


collection_name = 'documents'


def get_all_documents(request: Request):
    return get_all(request, collection_name)


def create_document(request: Request, data: dict):
    obj = data
    obj.created_at = get_current_utc_time()
    return create_one(request, data, collection_name)


def update_document(request: Request, data: dict, document_oid: str):
    parameter = {"_id": ObjectId(document_oid)}
    return update_one(request, data, collection_name, parameter)
