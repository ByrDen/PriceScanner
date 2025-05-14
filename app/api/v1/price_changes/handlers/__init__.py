from fastapi import APIRouter
from app.api.v1.price_changes.handlers import price_change_from_file


router = APIRouter(tags=["Price Change"])

router.include_router(price_change_from_file.router)