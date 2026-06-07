import heapq
import time

from app.registration.best_frame import BestFrame


class BestFrameCollector:

    def __init__(self, max_frames=5):

        self.max_frames = max_frames

        self.frames = []

    def reset(self):

        self.frames.clear()

    def add(self, frame, registration):

        score = registration["score"]

        item = (
            score,
            BestFrame(
                image=frame.copy(),
                score=score,
                timestamp=time.time(),
                pose=registration["pose"]
            )
        )

        if len(self.frames) < self.max_frames:

            heapq.heappush(self.frames, item)

            return

        if score > self.frames[0][0]:

            heapq.heapreplace(self.frames, item)

    def get_best_frames(self):

        return [

            frame

            for _, frame in

            sorted(

                self.frames,

                reverse=True

            )

        ]

    def is_complete(self):

        return len(self.frames) >= self.max_frames

    def count(self):

        return len(self.frames)