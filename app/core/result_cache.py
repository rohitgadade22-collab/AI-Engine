import threading


class ResultCache:

    def __init__(self):

        self._lock = threading.Lock()

        self._result = None

    def set_result(self, result):

        with self._lock:

            self._result = result

    def get_result(self):

        with self._lock:

            return self._result


result_cache = ResultCache()