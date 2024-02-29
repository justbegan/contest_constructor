from fastapi import Request
import jwt
from requests import request as r


def get_current_user(request: Request) -> dict:
    """
    {
        'token_type': 'access',
        'exp': 1710901923,
        'iat': 1708309923,
        'jti': '9e922af0fac34b93bec09c13a0a6de97',
        'user_id': 1
    }
    """
    secret_key = "django-insecure-02@4mn2!0a*2pn%eys0-4*6#&ey-i564q04!+vya!s_4zootb="
    authorization = request.headers.get("Authorization", None)
    if authorization is None:
        raise Exception("Unauthorized")
    if 'Bearer ' not in authorization:
        raise Exception("Token not found")
    token = authorization.replace('Bearer ', '')
    try:
        obj = jwt.decode(token, key=secret_key, algorithms=["HS256"])
        try:
            return obj['user_id']
        except Exception:
            raise Exception("user_id is not found in jwt")
    except jwt.ExpiredSignatureError as e1:
        raise Exception(e1)
    except jwt.InvalidTokenError as e2:
        raise Exception(e2)


def get_current_profile(request: Request, parameter: str = None) -> dict:
    url = 'http://127.0.0.1:8888/profile/api'
    response = r(
        method='GET',
        headers={
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Authorization": str(request.headers.get("Authorization"))
        },
        url=url
    )
    try:
        if parameter:
            return response.json()[parameter]
        else:
            return response.json()
    except:
        raise Exception("unauthorized or contest not selected")
