from fastapi.responses import JSONResponse
import logging


logging.basicConfig(
    filename="api_log.txt",
    filemode="a",
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
        logger.debug(log_message)


class Response_400(Base_response):
    def __call__(self, request, text: str):
        self.log(request, text, 400)
        return JSONResponse(
            {
                "status": False,
                "data": text
            }, status_code=400
        )


class Response_500(Base_response):
    def __call__(self, request, text):
        self.log(request, text, 400)
        return JSONResponse(
            {
                "status": False,
                "data": text
            }, status_code=500
        )


class Response_200():
    def __call__(self, data):
        return JSONResponse(
            {
                "status": True,
                "data": data
            }, status_code=200
        )
