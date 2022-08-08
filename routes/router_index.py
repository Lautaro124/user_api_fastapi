from fastapi import APIRouter

from routes import status, user

router = APIRouter()

router.include_router(status.router)
router.include_router(user.router)
