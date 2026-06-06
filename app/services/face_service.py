from insightface.app import FaceAnalysis
from loguru import logger

from app.services.base import BaseAIService


class FaceService(BaseAIService):

    def __init__(self):

        self.app = None

        self.initialized = False

    def initialize(self):

        logger.info("Loading InsightFace Model...")

        self.app = FaceAnalysis(
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=0,
            det_size=(640, 640)
        )

        self.initialized = True

        logger.info("Face Service Ready")

    def analyze(self, frame):

        faces = self.app.get(frame)

        result = []

        for face in faces:

            result.append({

                "confidence": float(face.det_score),

                "bbox": [

                    int(face.bbox[0]),

                    int(face.bbox[1]),

                    int(face.bbox[2]),

                    int(face.bbox[3])

                ]

            })

        return {

            "detected": len(result) > 0,

            "count": len(result),

            "faces": result

        }

    def health(self):

        return {

            "initialized": self.initialized

        }

    def shutdown(self):

        logger.info("Face Service Shutdown")