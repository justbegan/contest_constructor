from fastapi.routing import APIRouter
from fastapi import Request

from services.document import get_all_documents, create_document, update_document
from models.document import Documents


router = APIRouter(
    prefix='/docs',
    tags=['Документы']
)


@router.post("/create_document")
def create(request: Request, data: Documents):
    return create_document(request, data)


@router.get("/get_all")
def get_all(request: Request):
    return get_all_documents(request)


@router.put("/update_document")
def update(request: Request, data: Documents, document_oid: str):
    data = data.dict()
    return update_document(request, data, document_oid)
