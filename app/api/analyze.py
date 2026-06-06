from fastapi import APIRouter
from app.camera.camera_manager import camera_manager

router = APIRouter(tags=["Analyze"])


@router.post("/analyze")
def analyze():

    frame = camera_manager.get_frame()

    if frame is None:

        return {
            "success": False,
            "message": "No frame available"
        }

    height, width = frame.shape[:2]

    return {

        "success": True,

        "cameraConnected": True,

        "frameAvailable": True,

        "width": width,

        "height": height
    }