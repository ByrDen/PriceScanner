from collections.abc import AsyncIterator
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from typing import Protocol

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import sessionmaker
from app.models.base_db import session_context


class ActiveSession(Protocol):
    def __call__(self) -> AbstractAsyncContextManager[AsyncSession]:
        pass


@pytest.fixture(scope="session")
async def active_session() -> ActiveSession:
    @asynccontextmanager
    async def active_session_inner() -> AsyncIterator[AsyncSession]:
        async with sessionmaker() as session:
            session_context.set(session)
            yield session

    return active_session_inner # noqa