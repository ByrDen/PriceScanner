from typing import List

from pydantic import BaseModel, Field, ConfigDict


class InputSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sku: str = Field(max_length=9)
    barcode: List[str] = Field()
    name: str = Field(max_length=250)


class PatchSchema(BaseModel):
    sku: str | None = Field(default=None, max_length=9)
    barcode: List[str] | None = Field(default=None, min_length=1)
    name: str | None = Field(default=None, max_length=250)



class ResponseSchema(InputSchema):
    ...


class FullINfoResponseSchema(ResponseSchema):
    old_price: float | None = Field(default=None)
    new_price: float | None = Field(default=None)
