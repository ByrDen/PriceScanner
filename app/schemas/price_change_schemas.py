from pydantic import BaseModel


class InputSchema(BaseModel):
    sku: str
    name: str
    old_price: float | None
    new_price: float | None


class ResponseSchema(InputSchema):
    id: int


