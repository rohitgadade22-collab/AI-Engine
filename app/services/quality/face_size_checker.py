from app.services.quality.base_checker import BaseChecker


class FaceSizeChecker(BaseChecker):

    def name(self):

        return "face_size"

    def check(self, face_image, face_data):

        x1, y1, x2, y2 = face_data.bbox

        width = x2 - x1

        height = y2 - y1

        area = width * height

        passed = area > 35000

        return {

            "name": self.name(),

            "score": area,

            "passed": passed,

            "message": "Good" if passed else "Move Closer"

        }