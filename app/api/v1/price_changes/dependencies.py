from sqlalchemy import delete

from app.models import PriceChange
from app.models.base_db import db


async def clean_price_change_table() -> None:
    await db.session.execute(delete(PriceChange))
    await db.session.flush()


# CleanTable = Depends(clean_price_change_table)