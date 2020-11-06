import time


class Worker:

    # work_duration represents how long it takes the worker do to its task. (in seconds)
    def __init__(self, work_duration=10):
        self.work_duration = work_duration

    def work(self, number):
        time.sleep(self.work_duration)
        return number * number
