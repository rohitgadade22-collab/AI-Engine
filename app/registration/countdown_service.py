import time


class CountdownService:

    def __init__(self, duration=3):

        self.duration = duration
        self.start_time = None
        self.remaining = duration

    def reset(self):

        self.start_time = None
        self.remaining = self.duration

    def update(self):

        if self.start_time is None:
            self.start_time = time.time()

        elapsed = time.time() - self.start_time
        remaining = self.duration - elapsed
        self.remaining = round(max(0.0, remaining), 1)

        return remaining <= 0
