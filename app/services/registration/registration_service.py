from app.registration.best_frame_collector import BestFrameCollector
from app.registration.countdown_service import CountdownService
from app.services.managers.registration_session_manager import RegistrationSessionManager
from app.services.registration.registration_pipeline import RegistrationPipeline
from app.registration.stable_face_service import StableFaceService


class RegistrationService:

    def __init__(self):

        self.registration_manager = RegistrationSessionManager()

        self.stable_face_service = StableFaceService()

        self.countdown_service = CountdownService()

        self.best_frame_collector = BestFrameCollector()

        self.pipeline = RegistrationPipeline(
            registration_manager=self.registration_manager,
            stable_face_service=self.stable_face_service,
            countdown_service=self.countdown_service,
            best_frame_collector=self.best_frame_collector
        )

    def start(self, person_id: str, person_name: str):

        return self.registration_manager.start(
            person_id,
            person_name
        )

    def cancel(self):

        return self.registration_manager.cancel()

    def process(self, face_result):

        session = self.registration_manager.get_session()

        if session is None:
            return None

        return self.pipeline.process(
            face_result,
            session
        )

    def get_session(self):

        return self.registration_manager.get_session()

    def is_active(self):

        return self.registration_manager.is_active()


registration_service = RegistrationService()