import cv2

from app.services.overlay.draw_grid import draw_grid
from app.services.overlay.draw_face import draw_face
from app.services.overlay.draw_quality import draw_quality
from app.services.overlay.draw_instruction import draw_instruction


class OverlayService:

    def draw(self, frame, result):

        if frame is None:

            return None

        frame = draw_grid.draw(frame)

        face_result = result.get("face", {})

        if face_result.get("detected"):

            face = face_result["faces"][0]

            frame = draw_face.draw(

                frame,

                face

            )

            frame = draw_quality.draw(

                frame,

                face

            )

            frame = draw_instruction.draw(

                frame,

                face

            )

        return frame


overlay_service = OverlayService()