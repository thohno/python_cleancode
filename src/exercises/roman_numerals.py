class RomanNumerals:
    @staticmethod
    def convert_roman_numeral(roman_numeral: str):
        roman_dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        previous_value = 0
        for char in reversed(roman_numeral):
            value = roman_dictionary[char]
            if value <= previous_value:
                result -= value
            else:
                result += value
            previous_value = value
        return result