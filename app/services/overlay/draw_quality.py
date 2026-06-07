import cv2


class DrawQuality:

    def draw(self, frame, face):

        quality = face["quality"]

        y = 40

        for check in quality["checks"]:

            status = "OK" if check["passed"] else "FAIL"

            color = (

                (0, 255, 0)

                if check["passed"]

                else

                (0, 0, 255)

            )

            cv2.putText(

                frame,

                f"{check['name']} : {status}",

                (20, y),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.6,

                color,

                2

            )

            y += 30

        return frame


draw_quality = DrawQuality()