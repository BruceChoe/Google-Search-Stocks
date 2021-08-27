from pydantic import BaseSettings


# See api/config.py for instructions on how to override these for your personal
# environment.
class Settings(BaseSettings):
    testdb: str = "pytest"

    class Config:
        env_prefix = "petquery_"


settings = Settings()
