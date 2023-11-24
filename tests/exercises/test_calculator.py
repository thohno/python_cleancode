import unittest

from src.exercises.calculator import Calculator, LongRunningCalculation


class TestCalculator(unittest.TestCase):
    def test_calculate(self):
        calculator = Calculator(LongRunningCalculation())
        result = calculator.square_and_fancy_calculation(2)
        self.assertEqual(9, result)