# Code smell
def test_resistance():
    res = 1500
    mvo = 10
    mcu = 0.008
    mres = mvo / mcu
    assert mres < res


# Better
def test_resistance_better():
    max_resistance = 1500
    measured_voltage = 10
    measured_current = 0.008
    measured_resistance = measured_voltage / measured_current
    assert measured_resistance < max_resistance


if __name__ == '__main__':
    pass
