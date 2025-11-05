from pydantic import BaseModel

class BookCreate(BaseModel):
    event_type: str
    event_payload: str