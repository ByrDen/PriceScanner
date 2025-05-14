from starlette.testclient import TestClient

from tests.src.active_session import ActiveSession
from tests.src.assert_response import assert_response


async def test_product_creation(
        active_session: ActiveSession,
        client: TestClient,
) -> None:
    input_data = {}
    assert_response(
        client.post("/api/v1/products/",)
    )