import threading
import time

from loguru import logger

from app.camera.camera_manager import camera_manager
from app.core.orchestrator import orchestrator
from app.core.result_cache import result_cache
from app.events.event_generator import event_generator
from app.events.event_queue import event_queue
from app.services.registration.registration_service import registration_service


class AIWorker:

    def __init__(self):

        self.running = False
        self.thread = None

    def start(self):

        if self.running:
            return

        logger.info("Starting AI Worker")

        self.running = True

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

    def run(self):

        logger.info("AI Worker Started")

        while self.running:

            try:

                # ----------------------------------
                # Get Latest Camera Frame
                # ----------------------------------

                frame = camera_manager.get_frame()

                if frame is None:

                    time.sleep(0.05)
                    continue

                # ----------------------------------
                # AI Analysis
                # ----------------------------------

                result = orchestrator.analyze(frame)

                # ----------------------------------
                # Registration Processing
                # ----------------------------------

                if result["face"]["detected"]:

                    face_result = result["face"]["faces"][0]

                    registration_service.process(face_result)

                # ----------------------------------
                # Update Result Cache
                # ----------------------------------

                result_cache.set_result(result)

                # ----------------------------------
                # Generate Events
                # ----------------------------------

                events = event_generator.generate(result)

                for event in events:

                    event_queue.push(event)

                time.sleep(0.05)

            except Exception as ex:

                logger.exception(ex)

                time.sleep(0.10)

        logger.info("AI Worker Stopped")

    def stop(self):

        logger.info("Stopping AI Worker")

        self.running = False

        if self.thread:

            self.thread.join(timeout=2)


ai_worker = AIWorker()