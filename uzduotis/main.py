from fastapi import FastAPI, openapi
from fastapi.openapi.utils import get_openapi
from typing import List
from postgres_db import events, database
from models.event_request import EventRequest
from models.event_response import EventResponse
from models import exception_handlers
from models.exception_handlers import ErrorResponse
from models.status_code_handler import StatusOcdeHandler
import global_constants  as gc



def cutom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="persistence",
        version="0.0.1",
        description= "descr",
        routes = app.routes,

    )
    openapi_schema["openapi"] = "3.0.2"

app = FastAPI(title="persistence")
app.openapi = cutom_openapi()
openapi.utils.validation_error_response_definition = ErrorResponse.schema()
exception_handlers.include_exception_handlers(app=app)
status_code = StatusOcdeHandler()



class Config:
  orm_mode=True

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/event/", response_model=EventResponse, description= "event retriaval description", responses=status_code.get_code_dict(gc.DEFAULT_HTTPS_ERROR_CODES))
async def create_event(request: EventRequest):
    query = events.insert().values(event_type=request.event_type, event_payload=request.event_payload)
    last_event_id = await database.execute(query)

    query = events.select().where(events.c.id == last_event_id)
    inserted_event = await database.fetch_one(query)
    return inserted_event

@app.get("/event/", response_model=List[EventResponse], description= "event get method description")
async def get_events():
    query = events.select()
    return await database.fetch_all(query)

