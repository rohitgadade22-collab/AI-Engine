from app.services.quality.brightness_checker import BrightnessChecker
from app.services.quality.blur_checker import BlurChecker
from app.services.quality.brightness_checker import BrightnessChecker


class FaceQualityService:

    def __init__(self):

        self.checkers = [

            BlurChecker(),

            BrightnessChecker()

        ]

    def analyze(self, face_image, face_data):

        results = []

        for checker in self.checkers:

            results.append(

                checker.check(

                    face_image,

                    face_data

                )

            )

        passed = sum(

            1 for r in results

            if r["passed"]

        )

        score = int(

            (passed / len(results)) * 100

        )

        return {

            "score": score,

            "ready": score >= 80,

            "checks": results

        }