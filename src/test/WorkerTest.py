import unittest

from main.Worker import Worker


class TestWorker(unittest.TestCase):
    def test_worker_should_do_its_complicated_task(self):
        # GIVEN
        worker = Worker(20)
        number = 10
        expected_result = 100

        # WHEN
        result = worker.work(number)

        # THEN
        self.assertEqual(result, expected_result)
