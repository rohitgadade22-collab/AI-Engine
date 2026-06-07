from app.services.face.registration.registration_score import RegistrationScore
from app.services.face.registration.instruction_engine import InstructionEngine


class RegistrationPipeline:

    def __init__(self):

        self.registration_score = RegistrationScore()

        self.instruction_engine = InstructionEngine()

    def process(self, quality_result):

        checks = quality_result["checks"]

        score_result = self.registration_score.calculate(checks)

        instruction = self.instruction_engine.get_instruction(checks)

        return {

            "score": score_result["score"],

            "ready": score_result["ready"],

            "instruction": instruction

        }