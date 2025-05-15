from io import BytesIO

import numpy as np
import pandas as pd
from fastapi import UploadFile


async def get_changes_price_data_from_excel_file(file: UploadFile) -> dict[int, dict[str, str | float]]: # problem: so slow
    io_file = file.file.read()
    BytesIO().read()
    end_df = pd.read_excel( # noqa
        io_file,
        sheet_name=0,
        usecols="B:D",
        dtype={"sku": np.str_, "name": np.str_, "old_price": np.float64},
        na_filter=True,
    )

    start_df = pd.read_excel(   # noqa
        io_file,
        sheet_name=1,
        usecols="B:D",
        dtype={"sku": np.str_, "name": np.str_, "new_price": np.float64},
        na_filter=True
    )
    print(start_df)
    res_df = pd.merge(end_df, start_df, on=["sku", "name"], how="outer").replace({np.nan : None})
    print(res_df)
    res_dict = res_df.to_dict(orient="index")
    return res_dict