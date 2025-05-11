from fastapi import APIRouter

from app.api.v1.products.handlers import router as product_router
from app.api.v1.price_changes.handlers import router as price_change_router
router = APIRouter(prefix="/v1/")

router.include_router(product_router)
router.include_router(price_change_router)
