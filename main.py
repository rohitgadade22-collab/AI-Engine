from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.analyze import router as analyze_router
from app.api.status import router as status_router

from app.camera.camera_manager import camera_manager
from app.core.orchestrator import orchestrator


app = FastAPI(
    title="Perto AI Engine",
    version="1.0.0",
    description="Enterprise AI Engine"
)

# Register APIs
app.include_router(health_router, prefix="/api/v1")
app.include_router(analyze_router, prefix="/api/v1")
app.include_router(
    status_router,
    prefix="/api/v1"
)


@app.on_event("startup")
def startup():

    print("Starting Perto AI Engine...")

    camera_manager.start()

    orchestrator.initialize()

    print("Perto AI Engine Started")


@app.on_event("shutdown")
def shutdown():

    print("Stopping Perto AI Engine...")

    orchestrator.shutdown()

    camera_manager.stop()

    print("Perto AI Engine Stopped")


@app.get("/")
def root():

    return {

        "application": "Perto AI Engine",

        "version": "1.0.0",

        "status": "running"

    }