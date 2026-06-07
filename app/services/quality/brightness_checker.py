import cv2
import numpy as np

from app.services.quality.base_checker import BaseChecker


class BrightnessChecker(BaseChecker):

    def name(self):

        return "brightness"

    def check(self, face_image, face_data):

        gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

        score = np.mean(gray)

        return {

            "name": self.name(),

            "score": round(float(score), 2),

            "passed": 60 <= score <= 180,

            "message": "Good" if 60 <= score <= 180 else "Poor"

        }