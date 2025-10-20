"""
Walking skeleton for Car Charging Reservation System.
Minimal FastAPI application to get started with ATDD.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Car Charging Reservation System",
    description="ATDD Walking Skeleton",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Car Charging Reservation System"}


# TODO: Add your features here following ATDD approach:
# 1. Write a failing acceptance test
# 2. Write minimal code to make it pass
# 3. Refactor if needed
# 4. Repeat

# Example first feature:
# @app.get("/cars")
# async def get_cars():
#     """Get all cars"""
#     return []
