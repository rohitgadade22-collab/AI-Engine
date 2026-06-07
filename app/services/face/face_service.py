from insightface.app import FaceAnalysis
from loguru import logger

from app.services.base import BaseAIService
from app.models.face_result import FaceResult
from app.services.face.face_pipeline import FacePipeline


class FaceService(BaseAIService):

    def __init__(self):

        self.app = None

        self.initialized = False

        self.pipeline = FacePipeline()

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

        height, width = frame.shape[:2]

        for face in faces:

            x1 = max(0, int(face.bbox[0]))
            y1 = max(0, int(face.bbox[1]))
            x2 = min(width, int(face.bbox[2]))
            y2 = min(height, int(face.bbox[3]))

            if x2 <= x1 or y2 <= y1:
                logger.warning(
                    "Skipping invalid face bbox: %s",
                    face.bbox
                )
                continue

            face_image = frame[y1:y2, x1:x2]

            if face_image.size == 0:
                logger.warning(
                    "Skipping empty face crop for bbox: %s",
                    [x1, y1, x2, y2]
                )
                continue

            face_result = FaceResult(

                confidence=float(face.det_score),

                bbox=[x1, y1, x2, y2],

                landmarks=face.kps.tolist(),

                frame_width=width,

                frame_height=height,

                face_image=face_image

            )

            pipeline_result = self.pipeline.process(face_result)

            result.append({

                "confidence": face_result.confidence,

                "bbox": face_result.bbox,

                "quality": pipeline_result["quality"],

                "registration": pipeline_result["registration"],
                
                "registration_status": pipeline_result["registration_status"]

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