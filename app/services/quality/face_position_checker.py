from app.services.quality.base_checker import BaseChecker
from app.services.quality.registration_config import RegistrationConfig


class FacePositionChecker(BaseChecker):

    def name(self):

        return "face_position"

    def check(self, face_image, face_data):

        x1, y1, x2, y2 = face_data.bbox

        frame_width = face_data.frame_width
        frame_height = face_data.frame_height

        face_center_x = (x1 + x2) / 2
        face_center_y = (y1 + y2) / 2

        reg_left = frame_width * RegistrationConfig.LEFT
        reg_top = frame_height * RegistrationConfig.TOP
        reg_right = frame_width * RegistrationConfig.RIGHT
        reg_bottom = frame_height * RegistrationConfig.BOTTOM

        passed = (
            reg_left <= face_center_x <= reg_right
            and
            reg_top <= face_center_y <= reg_bottom
        )

        if passed:

            message = "Centered"

        else:

            if face_center_x < reg_left:

                message = "Move Right"

            elif face_center_x > reg_right:

                message = "Move Left"

            elif face_center_y < reg_top:

                message = "Move Down"

            else:

                message = "Move Up"

        score = 100 if passed else 0

        return {

            "name": self.name(),

            "score": score,

            "passed": passed,

            "message": message

        }