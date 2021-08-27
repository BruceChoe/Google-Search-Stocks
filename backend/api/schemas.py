from dustyapi.schemas import HALList, HALCreated, HALRetrieved, HALUpdated, HALDestroyed
from pydantic import BaseModel


# TODO: A nice-to-have would be some kind of helper that could define all the schemas
#       based on just a base schema, with a couple sensible overrides.
class DummyBase(BaseModel):
    size: str


class DummyConfigured(DummyBase):
    class Config:
        orm_mode = True

class DummyInput(DummyBase):
    pass

class DummyListed(DummyBase):
    class Header(DummyConfigured):
        pass

    class Config:
        orm_mode = True

class DummySingleton(DummyConfigured):
    id: int

dummy_schemas = {"input": DummyInput, "listed": DummyListed, "singleton": DummySingleton}
