import unittest
from unittest import TestCase

from src.exercises import roman_numerals as rn

class TestRomanNumerals(unittest.TestCase):
    def test_50_to_roman(self):
        output = rn.RomanNumerals.to_roman(50)
        self.assertTrue(output == 'VX', 'Incorrect roman numeral')