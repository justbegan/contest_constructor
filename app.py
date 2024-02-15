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
from routes.history import router as history_router
from core.responses import Response_500, Response_400


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
app.include_router(history_router)

app.mount('/media', StaticFiles(directory='media'), name='media')


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return Response_500()(request, str(e))


@app.middleware("http")
async def before_request_middleware(request: Request, call_next, authorization: str = Header(...)):
    secret_key = "django-insecure-02@4mn2!0a*2pn%eys0-4*6#&ey-i564q04!+vya!s_4zootb="
    authorization = request.headers.get("Authorization", "")
    if authorization is None:
        return Response_400()(request, "Unauthorized")
    if 'Bearer ' not in authorization:
        return Response_400()(request, "Token not found")
    token = authorization.replace('Bearer ', '')
    try:
        jwt.decode(token, key=secret_key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError as e1:
        return Response_500()(request, str(e1))
    except jwt.InvalidTokenError as e2:
        return Response_500()(request, str(e2))
    response = await call_next(request)
    return response
