from io import BytesIO

import numpy as np
import pandas as pd
from fastapi import UploadFile


async def get_products_data_from_excel_file(file: UploadFile) -> dict[int, dict[str, str]] | None:
    io_file = file.file.read()
    BytesIO().read()
    data_df = pd.read_excel(    # noqa
        io_file,
        sheet_name=0,
        # usecols="A:C",
        dtype={"barcode": np.str_, "sku": np.str_, "name": np.str_},
        na_filter=True,
    )
    res_dict = data_df.replace(np.nan, None).to_dict(orient="index")
    return res_dict
