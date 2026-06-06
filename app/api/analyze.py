from fastapi import APIRouter
from app.camera.camera_manager import camera_manager
from app.core.orchestrator import orchestrator

router = APIRouter(tags=["Analyze"])


@router.post("/analyze")
def analyze():

    frame = camera_manager.get_frame()

    if frame is None:

        return {
            "success": False,
            "message": "No frame available"
        }

    result = orchestrator.analyze(frame)

    return {

        "success": True,

        "camera": camera_manager.health(),

        "result": result

    }