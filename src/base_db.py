from collections.abc import Sequence
from contextvars import ContextVar
from typing import Any, Self

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

session_context: ContextVar[AsyncSession | None] = ContextVar("session", default=None)


class DBController:
    @property
    def session(self) -> AsyncSession:
        session = session_context.get()
        if session is None:
            raise ValueError("Session not initialized")
        return session

    async def get_first(self, stmt: Select[Any]) -> Any | None:
        return (await self.session.execute(stmt)).scalars().first()

    async def get_all(self, stmt: Select[Any]) -> Sequence[Any]:
        return (await self.session.execute(stmt)).scalars().all()


db: DBController = DBController()


class Base(DeclarativeBase):
    __tablename__: str

    @classmethod
    async def create(cls, **kwargs: Any) -> Self:
        entity =cls(**kwargs)
        db.session.add(entity)
        await db.session.flush()
        return entity

    @classmethod
    async def find_first_by_id(cls, *keys: Any) -> Self | None:
        return await db.session.get(cls, *keys)

    def update(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    async def delete(self) -> None:
        await db.session.delete(self)
        await db.session.flush()

    @classmethod
    def select_by_kwargs(cls, *order_by: Any, **kwargs: Any) -> Select[tuple[Any]]:
        if len(order_by) == 0:
            return select(cls).filter_by(**kwargs)
        return select(cls).order_by(*order_by).filter_by(**kwargs)

    @classmethod
    async def find_first_by_kwargs(cls, *order_by: Any, **kwargs: Any) -> Self | None:
        return await db.get_first(cls.select_by_kwargs(*order_by, **kwargs))

    @classmethod
    async def find_all_by_kwargs(cls, *order_by: Any, **kwargs: Any) -> Sequence[Self]:
        return await db.get_all(cls.select_by_kwargs(*order_by, **kwargs))
