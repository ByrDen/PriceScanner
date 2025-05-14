from fastapi import APIRouter

from app.api.v1.products.handlers import products_mub, products_from_file

router = APIRouter(tags=["Products"])

router.include_router(products_mub.router)
router.include_router(products_from_file.router)
