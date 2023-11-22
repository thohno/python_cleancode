import numpy as np

I = 4

MEDIAN = 1


# Rename
# Introduce variable/constant
# Change signature
# Extract method
# Go to declaration
# See usages
# Inline

# Value for stats:
# 1: median
# 2: squared
# 3. mean of squares
# 4. root
# else: mean
def process_data(column, stat):
    m = column.median()

    column.mean()

    if stat == MEDIAN:
      return m
    elif stat == 2:
        squared = np.square(column)
        return squared
    elif stat == 3:
        squared = np.square(column)
        mean_square = squared.mean()
        return mean_square
    elif stat == I:
        root_value = 2
        # adjustment factor
        a_f = 0.02
        return column ** (MEDIAN / root_value) - a_f
    else:
        return column.mean()


if __name__ == '__main__':
    pass