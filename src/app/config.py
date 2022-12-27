from typing import Any, List, Optional, Tuple, Union

from pydantic import AnyHttpUrl, BaseSettings, validator
from pydantic.env_settings import SettingsSourceCallable


class Settings(BaseSettings):
    FASTAPI_ROOT_PATH: str = ""
    API_V1_STR: str = "/v1"
    PROJECT_NAME: str = "HPDS Project"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    # SQLITE_URL: str = "sqlite:///./info.db"
    MYSQL_HOST: str = "db"
    MYSQL_PORT: str = "3306"
    MYSQL_USER: str = "root"
    MYSQL_PASS: str = "root"
    
    SQLALCHEMY_DATABASE_URI: str = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/hpds"
    
    
    
    # SQLALCHEMY_DATABASE_URI: str = "mysql+mysqlconnector://root:root@localhost:3306/hpds"
    
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> Tuple[SettingsSourceCallable, ...]:
            return env_settings, init_settings, file_secret_settings
    
    
settings = Settings()
