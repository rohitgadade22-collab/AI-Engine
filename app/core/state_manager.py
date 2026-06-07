import threading


class StateManager:

    def __init__(self):

        self._lock = threading.Lock()

        self._state = {}

    def get(self):

        with self._lock:

            return self._state.copy()

    def set(self, state):

        with self._lock:

            self._state = state.copy()


state_manager = StateManager()