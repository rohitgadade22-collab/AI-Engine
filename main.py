from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.analyze import router as analyze_router
from app.api.status import router as status_router
from app.workers.ai_worker import ai_worker

from app.camera.camera_manager import camera_manager
from app.core.orchestrator import orchestrator
from app.workers.sync_worker import sync_worker
from app.api.camera import router as camera_router


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
app.include_router(
    camera_router,
    prefix="/api/v1/camera"
)


@app.on_event("startup")
def startup():

    print("Starting Perto AI Engine...")

    camera_manager.start()

    orchestrator.initialize()

    ai_worker.start()

    sync_worker.start()

    print("Perto AI Engine Started")


@app.on_event("shutdown")
def shutdown():

    print("Stopping Perto AI Engine...")

    sync_worker.stop()

    ai_worker.stop()

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