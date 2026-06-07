import cv2


class DrawFace:

    def draw(self, frame, face):

        x1, y1, x2, y2 = face["bbox"]

        cv2.rectangle(

            frame,

            (x1, y1),

            (x2, y2),

            (255, 0, 0),

            2

        )

        return frame


draw_face = DrawFace()