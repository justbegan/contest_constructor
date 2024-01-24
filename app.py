# libs
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# end libs

from routes.statement import router as st_router
from routes.schema import router as sc_router
from routes.classificator import router as cl_router
from routes.contest import router as con_router
from routes.parameter import router as par_router


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


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
