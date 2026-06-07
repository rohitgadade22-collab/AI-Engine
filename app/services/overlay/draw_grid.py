import cv2


class DrawGrid:

    def draw(self, frame):

        h, w = frame.shape[:2]

        left = int(w * 0.25)
        right = int(w * 0.75)

        top = int(h * 0.10)
        bottom = int(h * 0.90)

        cv2.rectangle(

            frame,

            (left, top),

            (right, bottom),

            (0, 255, 0),

            2

        )

        return frame


draw_grid = DrawGrid()