import numpy as np

MEDIAN = 1
SQUARED = 2
MEAN_OF_SQUARES = 3
ROOT = 4


def process_data(column, stat):
    # rename variable
    median = column.median()

    # introduce constant
    if stat == MEDIAN:
        return median
    elif stat == SQUARED:
        return squared(column)
    elif stat == MEAN_OF_SQUARES:
        return mean_of_squares(column)
    elif stat == ROOT:
        return root(column)
    else:
        return column.mean()


# extract method, inline
def squared(column):
    return np.square(column)


def mean_of_squares(column):
    return np.square(column).mean()


def root(column):
    root_value = 2
    adjustment_factor = 0.02
    return column ** (1 / root_value) - adjustment_factor


if __name__ == '__main__':
    pass