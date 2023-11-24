import unittest

from parameterized import parameterized
from src.exercises.roman_numerals import RomanNumerals


class TestRomanNumerals(unittest.TestCase):
    @parameterized.expand([
        ('I', 1),
        ('II', 2),
        ('IV', 4),
        ('V', 5),
        ('IX', 9),
        ('X', 10),
        ('MCMXCIX', 1999)
    ])
    def test_convert_roman_numeral(self, roman_numeral, expected):
        result = RomanNumerals.convert_roman_numeral(roman_numeral)
        self.assertEqual(result, expected)
