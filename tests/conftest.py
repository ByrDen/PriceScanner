from collections.abc import Iterator


import pytest
from starlette.testclient import TestClient

from app.__main__ import app


@pytest.fixture(scope="session")
def client() -> Iterator[TestClient]:
    with TestClient(app) as client:
        yield client