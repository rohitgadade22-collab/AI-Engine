import threading
import time

from loguru import logger

from app.events.event_queue import event_queue


class SyncWorker:

    def __init__(self):

        self.running = False
        self.thread = None

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

        logger.info("Sync Worker Started")

    def run(self):

        while self.running:

            event = event_queue.pop()

            if event is None:

                time.sleep(0.5)

                continue

            # Currently just log it
            logger.info(f"SYNC EVENT : {event}")

            # Future:
            # requests.post(server_url,json=...)

    def stop(self):

        self.running = False

        if self.thread:

            self.thread.join(timeout=2)


sync_worker = SyncWorker()