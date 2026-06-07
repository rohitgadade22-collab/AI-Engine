import time


class StableFaceService:

    def __init__(self):

        self.start_time = None

    def process(self, registration):

        if registration["ready"]:

            if self.start_time is None:

                self.start_time = time.time()

            elapsed = time.time() - self.start_time

            if elapsed >= 2:

                return {

                    "stable": True,

                    "countdown": 0

                }

            return {

                "stable": False,

                "countdown": round(2 - elapsed, 1)

            }

        self.start_time = None

        return {

            "stable": False,

            "countdown": 2

        }

    def update(self, face_result):

        return self.process(face_result)


stable_face_service = StableFaceService()