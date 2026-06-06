from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="Perto AI Engine",
    version="1.0.0",
    description="Enterprise AI Engine"
)

app.include_router(health_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "application": "Perto AI Engine",
        "status": "running"
    }