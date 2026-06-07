from uuid import uuid4

from app.models.registration_session import RegistrationSession


class RegistrationSessionManager:

    def __init__(self):

        self._active_session = None

    def start(self, person_id: str, person_name: str):

        if self._active_session is not None:

            raise Exception("Registration already running")

        self._active_session = RegistrationSession(

            session_id=str(uuid4()),

            person_id=person_id,

            person_name=person_name

        )

        return self._active_session

    def get_session(self):

        return self._active_session

    def cancel(self):

        self._active_session = None

    def is_active(self):

        return self._active_session is not None