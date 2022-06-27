from distutils.debug import DEBUG
from pydantic import BaseSettings,Field

class EnvVariables(BaseSettings):
    SECRET_KEY: str
    DEBUG:bool

    class Config:
        env_file = '.env'

