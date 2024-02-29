# libs
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import Request
# end libs

from routes.statement import router as st_router
from routes.schema import router as sc_router
from routes.classificator import router as cl_router
from routes.contest import router as con_router
from routes.parameter import router as par_router
from routes.files import router as files_router
from routes.document import router as docs_router
from routes.history import router as history_router
from routes.comment import router as comment_router
from routes.news import router as news_router
from core.responses import Response_500
from services.fields.current_user import get_current_user


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
app.include_router(comment_router)
app.include_router(news_router)

app.mount('/media', StaticFiles(directory='media'), name='media')


@app.middleware("http")
async def before_request_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
    except Exception as e:
        return Response_500()(request, str(e))
    return response
