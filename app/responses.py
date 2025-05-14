from enum import Enum
from typing import Any

from fastapi import HTTPException
from starlette.responses import Response

ResponsesSchema = dict[str | int, dict[str, Any]]


class Responses(HTTPException, Enum):
    value: HTTPException

    @classmethod
    def responses(cls) -> ResponsesSchema:
        result: dict = {}
        for response in cls.__members__.values():
            error = response.value
            result[error.status_code] = {
                "description": error.detail,
                "content":{
                    "application/json": {
                        "example": {"detail": error.detail}
                    }
                }
            }

        return result