from fastapi import Request
from bson.objectid import ObjectId

from services.crud.create import create_one
from services.crud.get import get_all, get_all_method, get_one_method
from services.crud.delete import delete_one
from services.crud.update import update_one

from core.responses import Response_400


collection_name = 'parameters'


def create_parameter(request: Request, data: dict):

    if check_parameter_by_key(request, data) and check_parameter_by_title(request, data):
        return create_one(request, data, collection_name)
    else:
        return Response_400()(request, "parameter already exists")


def get_parameters(request: Request):
    return get_all(request, collection_name)


def delete_parameter_by_oid(request: Request, schema_oid: str):
    """
    Получить схему по id конкурса
    """
    try:
        parameter = {"_id": ObjectId(schema_oid)}
        schema = delete_one(request, collection_name, parameter)
        return schema
    except Exception as e:
        return Response_400()(request, str(e))


def check_parameter_by_title(request: Request, data: dict):
    """
    Проверка дубликатов по title
    """
    try:
        key = get_second_key(data)
        obj: dict = data.get(key, None)
        title = obj.get('title', None)
        all_docs = get_all_method(request, collection_name)
        for docs in all_docs:
            obj_title = docs[get_second_key(docs)]['title']
            if title == obj_title:
                return False
        return True
    except:
        return False


def check_parameter_by_key(request: Request, data: dict):
    """
    Проверка дубликатов по key
    """
    try:
        key = get_second_key(data)
        duplicate = get_one_method(request, collection_name, {key: {"$exists": True}})
        if duplicate is None:
            return True
        else:
            return False
    except:
        return False


def get_second_key(obj: dict):
    """
    получает второй ключ после '_id'
    """
    keys_except_id = [key for key in obj.keys() if key != "_id"]
    second_key = keys_except_id[0]
    return second_key


def update_parameter(request: Request, data: dict, parameter_oid: str):
    """
    Обновить параметер
    """
    parameter = {'_id': ObjectId(parameter_oid)}
    return update_one(request, data, collection_name, parameter)
