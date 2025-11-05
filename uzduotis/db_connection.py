from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import Optional 
from functools import lru_cache

class DatabaseSettings(BaseSettings):

    host: Optional[str] = Field(default= "localhost", description= "database host address", alias= "POSTGRE_HOST")
    db_name: Optional[str] = Field(default= "db_name", description= "database name", alias= "POSTGRE_DB_NAME")
    port: Optional[int] = Field(default= 800, description= "port number", alias= "POSTGRE_PORT")
    user: Optional[str] = Field(default= "temp_user", description= "database user name", alias= "POSTGRE_USER_NAME")
    password: Optional[str] = Field(default= "temp_pass", description= "database password", alias= "POSTGRE_PASSWORD")

    @field_validator("port", mode="before")
    @classmethod
    def validate_port(cls, v):
        """ensure port is an integer"""
        if v is None:
            return v
        return int(v)
    def get_credentials_dict(self) ->dict:
        return{
            "user": self.user,
            "host": self.host,
            "port": self.port,
            "password": self.password
        }
    
    def get_database_url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}/{self.db_name}"
    

    model_config = SettingsConfigDict(
        env_file =".env",
        env_file_encoding = "utf-8",
        case_sensitive=False,
        extra = "ignore"

    )

@lru_cache
def get_db_settings( )-> DatabaseSettings:
    """function to get DatabaseSettings singleton because lru decorator"""
    return DatabaseSettings()