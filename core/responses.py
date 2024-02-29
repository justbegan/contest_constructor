from fastapi.responses import JSONResponse
import logging
from datetime import datetime


logging.basicConfig(
    filename=f"logs/api log-{datetime.now():%Y-%m-%d}.txt",
    filemode="w",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)


class Base_response():
    def log(self, request, text, code):
        log_message = {
            "host": request.url.hostname,
            "endpoint": request.url.path,
            "text": text,
            "code": code
        }
        logger.error(log_message)


class Response_400(Base_response):
    def __call__(self, request, text: str) -> JSONResponse:
        self.log(request, text, 400)
        return JSONResponse(
            {
                "status": False,
                "data": text
            }, status_code=400
        )


class Response_500(Base_response):
    def __call__(self, request, text) -> JSONResponse:
        self.log(request, text, 400)
        return JSONResponse(
            {
                "status": False,
                "data": text
            }, status_code=500
        )


class Response_200():
    def __call__(self, data) -> JSONResponse:
        return JSONResponse(
            {
                "status": True,
                "data": data
            }, status_code=200
        )
