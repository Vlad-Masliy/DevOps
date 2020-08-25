import time


class timer:

    def __init__(self, name):
        self.name = name
        self._start = None

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exception_type, exception_value, traceback):
        end = time.time()
        duration = round(end - self._start, 3)
        print(f"block '{self.name}' executed in {duration} sec")


with timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)
