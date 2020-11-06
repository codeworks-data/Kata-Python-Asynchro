from main.Worker import Worker


class Factory:
    def __init__(self, workers_number):
        self.workers = []
        for i in range(workers_number):
            self.workers.append(Worker())

    def process_numbers(self, numbers):
        result = 0
        for index in range(len(numbers)):
            result += self.workers[index % len(self.workers)].work(numbers[index])
        return result
