from fastapi import Request
from .crud.get import get_all


collection_name = 'documents'


def get_all_documents(request: Request):
    return get_all(request, collection_name)
