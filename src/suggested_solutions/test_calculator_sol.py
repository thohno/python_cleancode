import unittest
from unittest.mock import MagicMock
from src.exercises.calculator import LongRunningCalculation, Calculator


# Reference: https://docs.python.org/3/library/unittest.mock.html
class TestFancyBusinessLogic(unittest.TestCase):
    def test_square(self):
        mocked_fancy_calculator = MagicMock()
        mocked_fancy_calculator.calculate.return_value = 5

        calculator = Calculator(mocked_fancy_calculator)
        result = calculator.square_and_fancy_calculation(2)
        self.assertEqual(9, result)
