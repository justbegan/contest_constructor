# libs
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Header
import jwt
from starlette.middleware.base import BaseHTTPMiddleware
# import uvicorn
# end libs

from routes.statement import router as st_router
from routes.schema import router as sc_router
from routes.classificator import router as cl_router
from routes.contest import router as con_router
from routes.parameter import router as par_router
from routes.files import router as files_router
from routes.document import router as docs_router
from core.responses import Response_500


config = dotenv_values(".env")

router = APIRouter()
app = FastAPI()
origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mongodb_client = MongoClient(
    config["ATLAS_URI"],
    username=config.get("DB_USER", None),
    password=config.get("DB_PASS", None)
)
app.database = app.mongodb_client[config["DB_NAME"]]
app.include_router(st_router)
app.include_router(sc_router)
app.include_router(cl_router)
app.include_router(con_router)
app.include_router(par_router)
app.include_router(files_router)
app.include_router(docs_router)

app.mount('/media', StaticFiles(directory='media'), name='media')


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


@app.middleware("http")
async def before_request_middleware(request: Request, call_next, authorization: str = Header(...)):
    secret_key = "django-insecure-6ci0z_eaq*aajt8!mb#%xtb5*ns65&22(jkx6*u^+9w+^h+&pe"
    authorization = request.headers.get("Authorization", "")
    if authorization is None:
        print("error 1")
    if 'Bearer ' not in authorization:
        print("error 2")
    token = authorization.replace('Bearer ', '')
    try:
        decoded_token = jwt.decode(token, key=secret_key, algorithms=["HS256"])

        print("Decoded Token:", decoded_token)
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")
    response = await call_next(request)
    return response


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            # Если возникает 500 ошибка, возвращаем JSON с описанием ошибки
            return Response_500()(request, str(e))
