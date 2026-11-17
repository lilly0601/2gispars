from fastapi import APIRouter

from app.api.dowloads_books.api_router import router as downloads
from app.api.auth.router import router as auth_router

router = APIRouter()

router.include_router(downloads, prefix="/parser", tags=["Parsers"])
router.include_router(auth_router, prefix="/auth", tags=["Authantificates"])