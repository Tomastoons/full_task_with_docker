from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

class NoDataError(Exception):
    def __init__(self, message):
        self.message = message

class ErrorResponse(BaseModel):
    content: str = Field(None, examples=["internal server error"] )

def custom_http_exception_handler(request, exc: HTTPException) ->JSONResponse:
    print(exc)
    return JSONResponse(status_code=exc.status_code, content=exc.detail)

def exception_handler(request, exc: Exception) ->JSONResponse:
    print(exc)
    return JSONResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content="Internal serveer error")

def no_data_error_handler(request, exc: NoDataError) ->JSONResponse:
    print(exc)
    return JSONResponse(status_code=HTTP_404_NOT_FOUND, content="no data")

def include_exception_handlers(app):
    app.add_exception_handler(HTTPException, custom_http_exception_handler)
    app.add_exception_handler(Exception, exception_handler)
    app.add_exception_handler(Exception, no_data_error_handler)

#TODO add more exceptions for database content and database errors, also impplementation errors and etc.

