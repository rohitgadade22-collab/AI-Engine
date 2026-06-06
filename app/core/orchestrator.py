from app.services.face_service import FaceService


class AIOrchestrator:

    def __init__(self):

        self.face_service = FaceService()

    def initialize(self):

        self.face_service.initialize()

    def analyze(self, frame):

        result = {}

        result["face"] = self.face_service.analyze(frame)

        return result

    def shutdown(self):

        self.face_service.shutdown()


orchestrator = AIOrchestrator()