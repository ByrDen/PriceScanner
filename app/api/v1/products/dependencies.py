from typing import Annotated

from fastapi import Path, Depends

from app.models import Product
from app.responses import Responses


class ProductResponses(Responses):
    PRODUCT_NOT_FOUND = 404, "Product not found"


async def retrieve_product_by_barcode(
    barcode: Annotated[str, Path()]
) -> Product:
    product = await Product.find_first_by_barcode(barcode=barcode)
    if product is None:
        raise ProductResponses.PRODUCT_NOT_FOUND
    return product

ProductByBarcode = Annotated[Product, Depends(retrieve_product_by_barcode)]
