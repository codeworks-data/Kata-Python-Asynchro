import unittest
import time

from main.Factory import Factory


class FactoryTest(unittest.TestCase):
    def test_process_numbers_should_return_unique_number_squared(self):
        # GIVEN
        factory = Factory(1)
        numbers = [2]
        expected_result = 4

        # WHEN
        result = factory.process_numbers(numbers)

        # THEN
        self.assertEqual(result, expected_result)

    def test_process_numbers_should_return_sum_of_squares(self):
        # GIVEN
        factory = Factory(5)
        numbers = [1, 2, 3, 4, 5]
        expected_result = 55

        # WHEN
        result = factory.process_numbers(numbers)

        # THEN
        self.assertEqual(result, expected_result)

    def test_process_numbers_should_parallelize_the_work(self):
        # GIVEN
        factory = Factory(5)
        numbers = [1, 2, 3, 4, 5]
        start_time = time.time()
        expected_time = 11

        # WHEN
        result = factory.process_numbers(numbers)

        # THEN
        self.assertLess(time.time() - start_time, expected_time)
