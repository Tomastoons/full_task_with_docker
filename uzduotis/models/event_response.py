#from pydantic import Field
from pydantic import BaseModel, Field

class EventResponse(BaseModel):
    id: int = Field(default = None, examples=50)
    event_type: str = Field(default = None, examples="message")
    event_payload: str = Field(default = None, examples="hello")