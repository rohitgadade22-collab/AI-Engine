from app.services.face_service import FaceService
from app.core.result_cache import result_cache


class AIOrchestrator:

    def __init__(self):

        self.face_service = FaceService()

    def initialize(self):

        self.face_service.initialize()

    def analyze(self, frame):

        result = {}

        result["face"] = self.face_service.analyze(frame)

        result_cache.set_result(result)

        return result

    def shutdown(self):

        self.face_service.shutdown()


orchestrator = AIOrchestrator()