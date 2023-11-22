from timeit import timeit
import numpy as np

def lists_numpy_comparison():
    measured_values = [23, 4, 55.6, 77.7, 23, 66.7, 26, 1.44] * 100
    average = sum(measured_values) / len(measured_values)
    print('List:', timeit(lambda: sum(measured_values) / len(measured_values), number=100000))

    measured_values = np.array(measured_values)
    numpy_average = measured_values.mean()
    print('Numpy:', timeit(measured_values.mean, number=100000))

    print('List Result:', average)
    print('Np Result:', numpy_average)

    # List: 3.819447329
    # Numpy: 0.7456985109999996
    # List Result: 34.68000000000186
    # Np Result: 34.68


if __name__ == '__main__':
    lists_numpy_comparison()