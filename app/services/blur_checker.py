import cv2

from app.services.quality.base_checker import BaseChecker


class BlurChecker(BaseChecker):

    def name(self):
        return "blur"

    def check(self, face_image, face_data):

        if face_image is None or face_image.size == 0:

            return {
                "name": self.name(),
                "score": 0,
                "passed": False,
                "message": "Invalid face"
            }

        gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

        score = cv2.Laplacian(gray, cv2.CV_64F).var()

        return {

            "name": self.name(),

            "score": round(float(score), 2),

            "passed": score > 100,

            "message": "Good" if score > 100 else "Blurred"

        }