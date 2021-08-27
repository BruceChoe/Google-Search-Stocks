from fastapi.testclient import TestClient
import pytest
from pytest_bdd import scenarios, given, when, then
from sqlalchemy import create_engine

from api import models
from api.dependencies import get_engine
from api.main import app
from api.config import settings
from tests.config import settings as test_settings

connection_string = (
    f"postgresql://{settings.dbuser}:{settings.dbpassword}"
    f"@{settings.dbhost}/{test_settings.testdb}"
)

scenarios("../features/queries.feature")


@pytest.fixture(scope="module")
def engine():
    engine_ = create_engine(connection_string, echo=True, future=True)

    yield engine_

    engine_.dispose()


@pytest.fixture(scope="module")
def connection(engine):
    connection_ = engine.connect()

    yield connection_

    connection_.close()


@pytest.fixture(autouse=True)
def transaction(connection):
    transaction = connection.begin()

    models.Base.metadata.create_all(connection)

    yield transaction

    transaction.rollback()


@given("I have not submitted any queries before", target_fixture="client")
def client(connection):
    app.dependency_overrides[get_engine] = lambda: connection

    return TestClient(app)


@when("I submit a query for a brown german shepherd")
def submit_query(client):
    client.post("/queries/", json={"color": "brown", "breed": "german shepherd"})


@then("I should have a single brown german shepherd in my list of queries")
def success_response(client):
    response_body = client.get("/queries/").json()

    queries = response_body["_embedded"]["doc:queries"]

    assert len(queries) == 1

    assert queries[0]["color"] == "brown"
    assert queries[0]["breed"] == "german shepherd"


@when("I do not submit a query")
def dont_submit_query(client):
    pass


@then("I should have nothing in my list of queries")
def empty_queries(client):
    response_body = client.get("/queries/").json()

    queries = response_body["_embedded"]["doc:queries"]

    assert len(queries) == 0
