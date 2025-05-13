from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from .base_db import Base
from ..schemas import price_change_schemas


class PriceChange(Base):
    # Child
    __tablename__ = "price_changes"

    sku: Mapped[str] = mapped_column(String(9), primary_key=True, autoincrement=False)
    old_price: Mapped[float | None] = mapped_column(Numeric(10, 2))
    new_price: Mapped[float | None] = mapped_column(Numeric(10, 2))

    InputSchema = price_change_schemas.InputSchema
    ResponseSchema = price_change_schemas.ResponseSchema