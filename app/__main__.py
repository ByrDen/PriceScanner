import asyncio
from collections.abc import Callable, Awaitable, AsyncIterator, Generator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from h11 import Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from app import api
from app.models.base_db import session_context
from app.config import sessionmaker
from app.setup_db import reinit_db


# @asynccontextmanager
def lifespan(_: FastAPI):
    asyncio.run(reinit_db())


app = FastAPI(
    title="Scanner",
    # lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.api_router)


@app.middleware("http")
async def db_session_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    async with sessionmaker.begin() as session:
        session_context.set(session)
        return await call_next(request)


if __name__ == '__main__':
    from uvicorn import run
    run(
        app=app,
        host="0.0.0.0",
        port=8000
        )
