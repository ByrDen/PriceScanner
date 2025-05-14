from typing import Any, Self

from sqlalchemy import String, ARRAY, UniqueConstraint, select, Row
from sqlalchemy.orm import Mapped, mapped_column

from app.models import PriceChange
from app.schemas import product_schemas
from app.models.base_db import Base, db


class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        UniqueConstraint("sku", "barcode"),
    )

    sku: Mapped[str] = mapped_column(String(9), primary_key=True, autoincrement=False)
    barcode: Mapped[list[str]] = mapped_column(ARRAY(String(13)))
    name: Mapped[str] = mapped_column(String(250))


    InputSchema = product_schemas.InputSchema
    PatchSchema =  product_schemas.PatchSchema
    ResponseSchema = product_schemas.ResponseSchema
    FullResponseSchema = product_schemas.FullINfoResponseSchema

    @classmethod
    async def find_first_by_barcode(cls, barcode: Any) -> Self | None:
        stmt = select(cls).filter(cls.barcode.any(barcode))
        return await db.get_first(stmt)

    @classmethod
    async def find_first_by_barcode_with_price(cls, barcode: Any) -> tuple[Self, PriceChange] | None:
        result = await cls.find_first_by_barcode(barcode=barcode)
        stmt = select(PriceChange).filter(PriceChange.sku==result.sku)
        changes = await db.get_first(stmt=stmt)
        return result, changes
    # async def add_barcode(self, barcode: Any) -> Self | None:
    #     if barcode not in self.barcode:
    #         self.barcode.append(barcode)
    #     else:
        # print(stmt.compile(compile_kwargs={"literal_binds": True}))
        # res = await db.get_first_row(stmt=stmt)
        # return res