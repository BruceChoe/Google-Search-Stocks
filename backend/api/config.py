from pydantic import BaseSettings


# To override these settings, populate the environment with variables of the same name
# and prefix. For example, if there is a class field here named `my_var`, and
# Config.env_prefix is `my_prefix_`, then you would override `my_var` by setting an
# environment variable of the name `my_prefix_my_var`.
class Settings(BaseSettings):
    dbuser: str = "petquery"
    dbpassword: str = "password"
    dbhost: str = "localhost"
    appdb: str = "appdb"
    dbsocket: str = None

    class Config:
        env_prefix = "petquery_"


settings = Settings()
