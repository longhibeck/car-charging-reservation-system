"""
Walking skeleton for Car Charging Reservation System.
Minimal FastAPI application to get started with ATDD.
"""

import os

from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from database import create_tables
from views.auth_views import router as auth_router
from views.car_views import router as car_router
from views.dashboard_views import router as dashboard_router

app = FastAPI(
    title="Car Charging Reservation System",
    description="ATDD Walking Skeleton",
    version="0.1.0",
)

create_tables()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(car_router)

static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/favicon.ico")
async def favicon():
    """Serve the favicon file"""
    favicon_path = os.path.join(os.path.dirname(__file__), "static", "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path, media_type="image/x-icon")
    return Response(content="", media_type="image/x-icon")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
