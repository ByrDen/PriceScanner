from fastapi import APIRouter, UploadFile, HTTPException
from starlette import status

from app.models import PriceChange
from app.models.base_db import db
from ..dependencies import clean_price_change_table
from ..utils import get_changes_price_data_from_excel_file


router = APIRouter()



@router.post(path="/products/change/file/upload",status_code=201)
async def upload_file_excel(
    file: UploadFile,
    clean_table: bool = False,
    ) -> dict[str, str]:
    if file.filename.split(sep=".")[1] not in ["xlsx", "xls"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect type of file")

    if clean_table:
        await clean_price_change_table()

    input_data = await get_changes_price_data_from_excel_file(file=file)

    for data in input_data.values():
        db.session.add(
            PriceChange(
                sku=data["sku"],
                old_price=data["old_price"],
                new_price=data["new_price"],
            )
        )
    await db.session.flush()

    return {"result": "OK"}





