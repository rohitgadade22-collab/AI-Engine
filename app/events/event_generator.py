from app.events.event import AIEvent


class EventGenerator:

    def __init__(self):

        self.previous_face_detected = False

    def generate(self, result):

        events = []

        current_face = result["face"]["detected"]

        # Face Appeared
        if current_face and not self.previous_face_detected:

            events.append(

                AIEvent(

                    event_type="FACE_DETECTED",

                    device_id="DEVICE001",

                    confidence=0.99,

                    data=result

                )

            )

        # Face Disappeared
        if not current_face and self.previous_face_detected:

            events.append(

                AIEvent(

                    event_type="FACE_LOST",

                    device_id="DEVICE001",

                    confidence=1.0,

                    data={}

                )

            )

        self.previous_face_detected = current_face

        return events


event_generator = EventGenerator()