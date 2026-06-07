from app.events.event import AIEvent


def main():

    event = AIEvent(

        event_type="FACE_DETECTED",

        device_id="DEVICE001",

        confidence=0.99

    )

    print(event)


if __name__ == "__main__":

    main()