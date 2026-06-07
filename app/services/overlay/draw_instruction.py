import cv2


class DrawInstruction:

    def draw(self, frame, face):

        registration = face["registration"]

        score = registration["score"]

        instruction = registration["instruction"]

        cv2.putText(

            frame,

            f"Registration Score : {score}%",

            (20, 220),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0, 255, 255),

            2

        )

        cv2.putText(

            frame,

            instruction,

            (20, 260),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0, 255, 0),

            2

        )

        return frame


draw_instruction = DrawInstruction()