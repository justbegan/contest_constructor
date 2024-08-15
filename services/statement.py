from fastapi import Request
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from bson.objectid import ObjectId

from core.responses import Response_400, Response_200

from .crud.update import update_one
from .crud.create import create_one_method
from .crud.get import get_all, get_one_method, get_pagination, get_one
from .history import create_history
from .fields.utctime import get_current_utc_time
from .fields.current_user import get_current_user
from .fields.new_status import new_status


def get_statements(
    request: Request,
    contest_oid: str,
    page: int,
    page_size: int,
    parameter: dict = {},
    regular: str = None
):
    """
    Получить все заявки по oid конкурса
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    if regular:
        """поиск по регулярному выражению"""
        parameter["$or"] = [
            {field: {"$regex": regular, "$options": "i"}
             } for field in get_one_method(request, collection_name, {}).keys()
        ]
    return get_pagination(request, collection_name, page, page_size, parameter)


def get_statements_by_id(request: Request, contest_oid: str, statement_oid: str):
    """
    Получить заявку по id
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    return get_one(request, collection_name, {'_id': ObjectId(statement_oid)})


def get_statements_by_user(request: Request, contest_oid: str, user_oid: str):
    """
    Получить все заявки по oid конкурса и oid пользователя
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    return get_all(request, collection_name, {"user_oid": user_oid})


def create_statement(request: Request, contest_oid: str, data: dict):
    """
    Создает заявку
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    try:
        schema = get_schema_for_statement(request, contest_oid)
    except Exception as e:
        return Response_400()(request, str(e))

    data['created_at'] = get_current_utc_time()
    data['user_oid'] = get_current_user(request)
    data['status'] = new_status(request, contest_oid)

    try:
        data = {key: value for key, value in data.items() if key in schema.get("properties", {}) and value != ''}
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return Response_400()(request, e.message)
    created_statement = create_one_method(request, data, collection_name)
    create_history(request, created_statement['_id'], 'Заявка создана')
    return Response_200()(created_statement)


def update_stamement(request: Request, statement_oid: str, data: dict, contest_oid: str):
    """
    Обновляет заявку
    """
    collection_name = get_contest_collection_name(request, contest_oid)
    try:
        schema = get_schema_for_statement(request, contest_oid)
    except Exception as e:
        return Response_400()(request, str(e))
    try:
        data = {key: value for key, value in data.items() if key in schema.get("properties", {}) and value != ''}
        validate(instance=data, schema=get_mutated_schema(schema, data))
    except ValidationError as e:
        return Response_400()(request, str(e))
    parameter = {'_id': ObjectId(statement_oid)}

    check_status(request, statement_oid, collection_name, data)

    return update_one(request, data, collection_name, parameter)


def get_mutated_schema(schema: dict, data: dict):
    """
    Получить урезанную схему, чтобы валедировать только отправленные поля
    если front отправил status я проверяю и обновляю только это поле
    """
    try:
        new_properties = {}
        new_required = []
        for key, value in schema['properties'].items():
            if key in data:
                new_properties[key] = value
        for i2 in schema['required']:
            if i2 in data:
                new_required.append(i2)
        schema['properties'] = new_properties
        schema['required'] = new_required
    except:
        pass
    return schema


def get_schema_for_statement(request: Request, contest_oid: str):
    schema = get_one_method(request, 'schemas', {"contest_oid": contest_oid})
    if schema is None:
        raise Exception("Schemas not found")
    return schema


def get_contest_collection_name(request: Request, contest_oid: str):
    contest = get_one_method(request, 'contests', {"_id": ObjectId(contest_oid)})
    if contest is None:
        raise Exception("Contests not found")
    return contest.get("unique_name")


def check_status(request: Request, statement_oid: str, collection_name: str, data: dict):
    """
    Провекрка, изменился ли статус
    """
    st = get_one_method(request, collection_name, {'_id': ObjectId(statement_oid)})
    if st is None:
        raise Exception("status not found")
    old_status = st.get('status', None)
    new_status = data.get('status', None)
    if old_status is None or new_status is None:
        return None
    if old_status != new_status:
        try:
            new_status_obj = get_one_method(request, 'classificators', {"_id": ObjectId(new_status['class'])})
            if new_status_obj is None:
                raise Exception("status not found")
            new_status_value = new_status['value']
            new_status_title = list(filter(lambda x: new_status_value == x['id'], new_status_obj['data']))[0]['title']
        except:
            new_status_title = 'None'
        create_history(request, statement_oid, f"Статус изменился на '{new_status_title}'")
