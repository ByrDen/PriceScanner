from collections.abc import Callable, Awaitable

from fastapi import FastAPI
from h11 import Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from app import api
from src.base_db import session_context
from src.config import sessionmaker

app = FastAPI(
    title="Scanner",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(
    request: Request,
    call_next: Callable[Request, Awaitable[Response]],
) -> Response:
    async with sessionmaker.begin() as session:
        session_context.set(session)
        return await call_next(request)


app.include_router(api.api_router)


if __name__ == '__main__':
    from uvicorn import run
    run(
        app=app,
        host="0.0.0.0",
        port=8000
        )
