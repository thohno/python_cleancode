import time


class Calculator:
    def __init__(self, fancy_calculator):
        self.fancy_calculator = fancy_calculator

    def square_and_fancy_calculation(self, i):
        result = i ** 2
        result += self.fancy_calculator.calculate(7)
        return result


class LongRunningCalculation:

    def calculate(self, value):
        # Do some super long running calculation
        time.sleep(value)
        return 5


if __name__ == '__main__':
    pass
