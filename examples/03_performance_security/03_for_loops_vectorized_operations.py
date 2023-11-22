from timeit import timeit
import numpy as np

def for_loops_vectorized_comparison():
    measured_values = [23, 4, 55.6, 77.7, 23, 66.7, 26, 1.44] * 1000
    result = [value * 20 for value in measured_values]
    print('List:', timeit(lambda: [value * 20 for value in measured_values], number=10000))

    measured_values = np.array(measured_values)
    np_result = measured_values * 20
    print('Numpy:', timeit(lambda: measured_values * 20, number=10000))

    print('List Result:', result)
    print('Np Result:', np_result)

    # List: 4.185107427
    # Numpy: 0.03139949899999994
    # List Result: [460, 80, 1112.0, 1554.0, 460, 1334.0, 520, 28.799999999999997, ...
    # Np Result: [ 460.    80.  1112.  ... 1334.   520.    28.8]


if __name__ == '__main__':
    for_loops_vectorized_comparison()