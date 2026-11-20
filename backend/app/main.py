
from fastapi import FastAPI

from app.api.category import router as category_router

app = FastAPI(
    title="StitchStock API",
    description="Inventory Management System for a Textile Shop",
    version="1.0.0"
)

# Register API routers
app.include_router(category_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to StitchStock API!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "StitchStock"
    }
