from json import JSONDecodeError
from typing import Any

from httpx import Response


def assert_contains(real: dict[str, Any], expected: dict[str, Any]) -> None:
    assert real.get("status_code") == expected.get("status_code")
    assert real.get("headers") == expected.get("headers")
    assert real.get("status_code") == expected.get("status_code")
    assert real.get("status_code") == expected.get("status_code")


def assert_response(
    response: Response,
    *,
    expected_code: int = 200,
    expected_json: dict[str, Any],
    expected_headers: dict[str, Any] | None = None,
    expected_cookies:dict[str, Any] | None = None
) -> Response:
    try:
        json_data = response.json()
    except (UnicodeDecodeError, JSONDecodeError):
        json_data = None

    expected_headers = expected_headers or {}
    expected_headers.setdefault("Content-Type", "application/json")
    assert_contains(
        {
            "status_code": response.status_code,
            "headers": response.headers,
            "cookies": response.cookies,
            "json_data": json_data,
        },
        {
            "status_code": expected_code,
            "headers": expected_headers,
            "cookies": expected_cookies or {},
            "json_data": expected_json,
        }
    )

    return response


def assert_nodata_response(
    response: Response,
    *,
    expected_code: int = 204,
    expected_headers: dict[str, Any] | None = None,
    expected_cookies:dict[str, Any] | None = None
) -> Response:
    try:
        json_data = response.json()
    except (UnicodeDecodeError, JSONDecodeError):
        json_data = None

    expected_headers = expected_headers or {}
    expected_headers.setdefault("Content-Type", "application/json")
    assert_contains(
        {
            "status_code": response.status_code,
            "headers": response.headers,
            "cookies": response.cookies,
            "json_data": json_data,
        },
        {
            "status_code": expected_code,
            "headers": expected_headers,
            "cookies": expected_cookies or {},
            "json_data": None,
        }
    )

    return response
