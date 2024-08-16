from fastapi.routing import APIRouter
from fastapi import Request

from services.document import get_all_documents, create_document
from models.document import Documents


router = APIRouter(
    prefix='/docs',
    tags=['Документы']
)


@router.post("/create_document")
def create(request: Request, data: Documents):
    return create_document(request, data)


@router.get("/")
def get_all(request: Request):
    return get_all_documents(request)
