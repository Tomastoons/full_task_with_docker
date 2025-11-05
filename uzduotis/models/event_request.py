from pydantic import Field, BaseModel, ConfigDict

class EventRequest(BaseModel):
    event_type: str = Field(default = None, examples="message")
    event_payload: str = Field(default = None, examples="hello")
    model_config = ConfigDict(extra="forbid")