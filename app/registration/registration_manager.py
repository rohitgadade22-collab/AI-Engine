from app.registration.registration_state import RegistrationState
from app.registration.stable_face_service import stable_face_service


class RegistrationManager:

    def process(self, registration):

        if not registration["ready"]:

            return {

                "state": RegistrationState.ALIGN_FACE.value,

                "instruction": registration["instruction"],

                "countdown": 0

            }

        stable = stable_face_service.process(

            registration

        )

        if stable["stable"]:

            return {

                "state": RegistrationState.READY.value,

                "instruction": "READY",

                "countdown": 0

            }

        return {

            "state": RegistrationState.HOLD_STILL.value,

            "instruction": "Hold Still",

            "countdown": stable["countdown"]

        }


registration_manager = RegistrationManager()