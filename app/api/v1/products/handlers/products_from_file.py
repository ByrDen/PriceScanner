
from fastapi import APIRouter, UploadFile, HTTPException
from starlette import status

from app.api.v1.products.utils import get_products_data_from_excel_file
from app.models import Product
from app.models.base_db import db

router = APIRouter()


@router.post(
    path="/products/file/upload/",
    status_code=201,
)
async def add_products_from_file(
    file: UploadFile
) -> dict[str, str]:
    if file.filename.split(sep=".")[1] not in ["xlsx", "xls"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect type of file")

    input_data = await get_products_data_from_excel_file(file=file)

    for data in input_data.values():
        db.session.add(Product(
            sku=data["sku"],
            barcode=data["barcode"].split(),
            name=data["name"]
        ))

    await db.session.flush()

    return {"result": "OK"}