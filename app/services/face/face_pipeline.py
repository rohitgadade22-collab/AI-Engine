from app.services.quality.quality_service import QualityService
from app.services.face.registration.registration_pipeline import RegistrationPipeline
from app.registration.registration_manager import registration_manager


class FacePipeline:

    def __init__(self):

        self.quality_service = QualityService()

        self.registration_pipeline = RegistrationPipeline()

    def process(self, face_result):

        # ----------------------------
        # Quality
        # ----------------------------

        quality = self.quality_service.analyze(

            face_result.face_image,

            face_result

        )

        # ----------------------------
        # Registration Score
        # ----------------------------

        registration = self.registration_pipeline.process(

            quality

        )

        # ----------------------------
        # Registration State
        # ----------------------------

        registration_status = registration_manager.process(

            registration

        )

        return {

            "quality": quality,

            "registration": registration,

            "registration_status": registration_status

        }