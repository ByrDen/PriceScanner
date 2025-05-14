# import asyncio
# import faulthandler

from app.config import engine
from app.models import Base


async def reinit_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# if __name__ == '__main__':
#     faulthandler.enable()
#     asyncio.run(reinit_db())
