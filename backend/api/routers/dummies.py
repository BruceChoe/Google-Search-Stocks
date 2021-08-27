from dustyapi import DustyRouter

from api import models, schemas


router = DustyRouter(
    rel="dummies", universe=models.DummyUniverse(), schemas=schemas.dummy_schemas
)


@router.list()
def list_dummies():
    pass


@router.create()
def create_dummy():
    pass


@router.retrieve()
def retrieve_dummy():
    pass


@router.update()
def update_dummy():
    pass


@router.destroy()
def destroy_dummy():
    pass
