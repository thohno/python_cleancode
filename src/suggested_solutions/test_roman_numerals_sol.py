import unittest
from parameterized import parameterized

from src.exercises import roman_numerals as rn

class TestRomanNumerals(unittest.TestCase):
    def test_50_to_roman(self):
        output = rn.RomanNumerals.to_roman(50)
        self.assertTrue(output == 'L', 'Incorrect roman numeral')

    def test_6_to_roman(self):
        output = rn.RomanNumerals.to_roman(6)
        self.assertTrue(output == 'VI', 'Incorrect roman numeral')

    @parameterized.expand([
        (1, 'I'),
        (4, 'IV'),
        (9, 'IX'),
        (40, 'XL'),
        (90, 'XC'),
        (500, 'D'),
        (1000, 'M'),
        (3999, 'MMMCMXCIX')
    ])
    def test_to_roman(self, input_value, expected_output):
        result = rn.RomanNumerals.to_roman(input_value)
        self.assertEqual(result, expected_output)
