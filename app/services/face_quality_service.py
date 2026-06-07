import cv2
import numpy as np


class FaceQualityService:

    def analyze(self, frame, face):

        x1, y1, x2, y2 = map(int, face.bbox)

        face_img = frame[y1:y2, x1:x2]

        if face_img.size == 0:

            return {

                "quality": 0,

                "ready": False

            }

        gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

        blur_score = cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()

        brightness = np.mean(gray)

        return {

            "blur": round(float(blur_score), 2),

            "brightness": round(float(brightness), 2)

        }