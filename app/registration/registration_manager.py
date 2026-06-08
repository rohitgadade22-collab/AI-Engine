from app.registration.registration_state import RegistrationState
from app.registration.stable_face_service import stable_face_service
from app.registration.countdown_service import CountdownService


class RegistrationManager:

    def __init__(self):

        self.countdown_service = CountdownService()

    def process(self, registration):

        if not registration["ready"]:

            self.countdown_service.reset()

            return {

                "state": RegistrationState.ALIGN_FACE.value,

                "instruction": registration["instruction"],

                "countdown": 0

            }

        stable = stable_face_service.process(registration)

        if not stable["stable"]:

            self.countdown_service.reset()

            return {

                "state": RegistrationState.HOLD_STILL.value,

                "instruction": "Hold Still",

                "countdown": stable["countdown"]

            }

        completed = self.countdown_service.update()

        if not completed:

            return {

                "state": RegistrationState.READY_TO_CAPTURE.value,

                "instruction": "Get Ready",

                "countdown": self.countdown_service.remaining

            }

        return {

            "state": RegistrationState.CAPTURING.value,

            "instruction": "Capturing",

            "countdown": 0

        }


registration_manager = RegistrationManager()