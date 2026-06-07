import cv2
import threading
import time
from loguru import logger


class CameraManager:

    def __init__(self):
        self.cap = None
        self.running = False
        self.frame = None
        self.lock = threading.Lock()
        self.thread = None

    def start(self):

        logger.info("Initializing Camera")

        # Use DirectShow backend
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not self.cap.isOpened():

            logger.error("Camera not found")
            return

        # Request HD resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        # Request FPS
        self.cap.set(cv2.CAP_PROP_FPS, 30)

        # Enable autofocus if supported
        self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        # Reduce buffering
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        logger.info(
            f"Camera Resolution : "
            f"{self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)} x "
            f"{self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}"
        )

        logger.info(
            f"Camera FPS : "
            f"{self.cap.get(cv2.CAP_PROP_FPS)}"
        )

        self.running = True

        self.thread = threading.Thread(
            target=self.update,
            daemon=True
        )

        self.thread.start()

        logger.info("Camera Started Successfully")

    def stop(self):

        logger.info("Stopping Camera")

        self.running = False

        if self.thread:

            self.thread.join(timeout=1)

        if self.cap:

            self.cap.release()

        logger.info("Camera Stopped")

    def update(self):

        while self.running:

            success, frame = self.cap.read()

            if success:

                with self.lock:

                    self.frame = frame

            time.sleep(0.01)


    def get_frame(self):

        with self.lock:

            if self.frame is None:
                return None

            return self.frame.copy()

    def health(self):
        return {

            "connected": self.cap is not None and self.cap.isOpened(),

            "running": self.running,

            "frameAvailable": self.frame is not None
        }


camera_manager = CameraManager()