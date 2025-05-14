from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Query

from app.api.v1.products.dependencies import ProductByBarcode, ProductResponses
from app.models.product_db import Product

router = APIRouter()


@router.get(
    path="/products/",
    response_model=list[Product.ResponseSchema],
    summary="List Paginated products"
)
async def list_products(
    limit: Annotated[int, Query(gt=0, le=50)] = 10,
    offset: Annotated[int, Query(gt=0, le=50)] = 0,
) -> Sequence[Product]:
    return await Product.find_paginated_by_kwargs(offset=offset, limit=limit)


@router.post(
    path="/products/",
    status_code=201,
    response_model=Product.ResponseSchema,
    summary="Create a new product"
)
async def create_product(
    input_data: Product.InputSchema
) -> Product:
    return await Product.create(**input_data.model_dump())


@router.get(
    path="/products/{barcode}/",
    response_model=Product.ResponseSchema,
    responses=ProductResponses.responses(),
    summary="Retrieve product by id",
)
async def retrieve_product(
    product: ProductByBarcode,
) -> Product:
    return product


@router.patch(
    path="/products/{barcode}/",
    response_model=Product.ResponseSchema,
    responses=ProductResponses.responses(),
    summary="Update product by id",
)
async def patch_product(
    product: ProductByBarcode,
    patch_data: Product.PatchSchema,
) -> Product:
    product.update(**patch_data.model_dump(exclude_defaults=True))
    return product


@router.delete(
    path="/products/{barcode}/",
    status_code=204,
    responses=ProductResponses.responses(),
    summary="Delete product by id"
)
async def delete_product(product: ProductByBarcode) -> None:
    await product.delete()