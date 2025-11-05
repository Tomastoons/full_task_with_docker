from pydantic import BaseModel, Field
from typing import Optional

class Ok(BaseModel):
    content: str = Field(examples=["ok"])

class Created(BaseModel):
    content: str = Field(examples=["Creaded"]) 

HTTP_200_STATUS_MODEL_DIC = {
    200: {"model": Ok},
    201: {"model": Created}
}

####    400 #########
class BadRequest(BaseModel) :
    content: str = Field(examples=["Bad request"]) 

class NotFound(BaseModel) :
    content: str = Field(examples=["Not found"])

class RequestTimeout(BaseModel) :
    content: str = Field(examples=["request Timeout"])  

HTTP_400_STATUS_MODEL_DIC = {
    400: {"model": BadRequest},
    404: {"model": NotFound},
    408: {"model": RequestTimeout}
}

####    500 #########

class InternalServerError(BaseModel):
    content: str = Field(examples=["Internal Server Error"])  

HTTP_500_STATUS_MODEL_DIC = {
    500: {"model": InternalServerError}
}

class StatusOcdeHandler():
    def __init__(self):
        self.code_dict ={}
        self.code_dict.update(HTTP_200_STATUS_MODEL_DIC)
        self.code_dict.update(HTTP_400_STATUS_MODEL_DIC)
        self.code_dict.update(HTTP_500_STATUS_MODEL_DIC)
    
    def get_code_dict(self, code_list: Optional[list] = None) ->dict :
        return_dict = {}
        if code_list is None:
            for code in code_list:
                return_dict[code] = self.code_dict[code]
            return return_dict
        else:
            return self.code_dict
        

        #TODO more status codes 