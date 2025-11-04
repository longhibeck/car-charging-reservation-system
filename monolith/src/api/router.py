from fastapi import APIRouter

from api.routes.auth import router as auth_router
from api.routes.cars import router as cars_router

# Main API router that combines all sub-routers with versioning
router = APIRouter(
    prefix="/api/v1", tags=["v1"], responses={404: {"description": "Not found"}}
)

# Include all route modules
router.include_router(auth_router)
router.include_router(cars_router)
