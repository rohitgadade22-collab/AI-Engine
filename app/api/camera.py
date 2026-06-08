from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import cv2
import time

from app.camera.camera_manager import camera_manager
from fastapi.responses import Response

from app.core.result_cache import result_cache
from app.services.overlay.overlay_service import overlay_service

router = APIRouter(
    tags=["Camera"]
)


def generate():

    while True:

        frame = camera_manager.get_frame()
        result = result_cache.get_result()

        if result:
            frame = overlay_service.draw(

            frame,

            result

        )

        if frame is None:
            time.sleep(0.01)
            continue

        ret, buffer = cv2.imencode(
            ".jpg",
            frame,
            [
                cv2.IMWRITE_JPEG_QUALITY,
                100
            ]
        )

        if not ret:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )

        # Limit to ~30 FPS
        time.sleep(0.033)


@router.get("/snapshot")
def snapshot():

    frame = camera_manager.get_frame()

    if frame is None:
        return Response(status_code=404)

    ret, buffer = cv2.imencode(
        ".jpg",
        frame,
        [cv2.IMWRITE_JPEG_QUALITY, 100]
    )

    return Response(
        content=buffer.tobytes(),
        media_type="image/jpeg"
    )

@router.get("/live")
def live():

    return StreamingResponse(
        generate(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )