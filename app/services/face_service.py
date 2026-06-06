from loguru import logger
from app.services.base import BaseAIService


class FaceService(BaseAIService):

    def __init__(self):

        self.initialized = False

    def initialize(self):

        logger.info("Initializing Face Service")

        self.initialized = True

    def analyze(self, frame):

        return {
            "detected": False,
            "count": 0,
            "faces": []
        }

    def health(self):

        return {
            "initialized": self.initialized
        }

    def shutdown(self):

        logger.info("Shutting down Face Service")