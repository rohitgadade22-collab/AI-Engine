from queue import Queue


class EventQueue:

    def __init__(self):
        self.queue = Queue()

    def push(self, event):
        self.queue.put(event)

    def pop(self):
        if self.queue.empty():
            return None

        return self.queue.get()

    def size(self):
        return self.queue.qsize()

    def is_empty(self):
        return self.queue.empty()

    def clear(self):
        while not self.queue.empty():
            self.queue.get()


# Singleton object
event_queue = EventQueue()