from fastapi.routing import APIRouter
from fastapi import Request
from services.parameter import create_parameter, get_parameters, delete_parameter_by_oid, update_parameter


router = APIRouter(
    prefix='/parameter',
    tags=['Параметры']
)


@router.post("/create_parameter")
def create(request: Request, data: dict):
    """
    Создание параметра
    """
    return create_parameter(request, data)


@router.get("/get_parameters")
def get(request: Request):
    """
    Получить все параметры
    """
    return get_parameters(request)


@router.delete("/delete_parameter")
def delete(request: Request, parameter_oid: str):
    """
    Удалить параметр по oid
    """
    return delete_parameter_by_oid(request, parameter_oid)


@router.put("/update_parameter")
def update(request: Request, data: dict, parameter_oid: str):
    return update_parameter(request, data, parameter_oid)
