from fastapi import FastAPI
from app.api.health import router as health_router
from app.camera.camera_manager import camera_manager
from app.api.analyze import router as analyze_router

app = FastAPI(
    title="Perto AI Engine",
    version="1.0.0"
)

app.include_router(
    analyze_router,
    prefix="/api/v1"
)


@app.on_event("startup")
def startup():

    camera_manager.start()


@app.on_event("shutdown")
def shutdown():

    camera_manager.stop()


@app.get("/")
def root():

    return {
        "application": "Perto AI Engine",
        "status": "running"
    }