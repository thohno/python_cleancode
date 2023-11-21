import numpy as np
import pandas as pd

# Rename
# Introduce variable/constant
# Change signature
# Extract method
# Go to declaration
# See usages

# Click Go To Declaration for the following method
# Try to change method signature of the following method to use 'SQUARED' as the default value for stat
def process_data(column, stat):
    squared = np.square(column)
    # Rename the following variable
    m = column.median()

    # Introduce variable here
    column.mean()

    # Extract this method
    def calculate_mean_of_squares(column, squared_values):
      mean_square = squared_values.mean()
      return mean_square

    # Extract this method
    def calculate_root(column):
        root_value = 3
        adjustment_factor = 0.02
        return column ** 1/root_value - adjustment_factor

    # Introduce constants here, instead of using magic strings
    if stat == 'MEDIAN':
      return m
    elif stat == 'SQUARED':
        return squared
    elif stat == 'MEAN OF SQUARES':
        # Introduce a new variable here
       return calculate_mean_of_squares(column, squared)
    elif stat == 'ROOT':
        return calculate_root(column)
    else:
        return column.mean()


if __name__ == '__main__':  
  df = pd.DataFrame({'day1': [1, 2, 3, 4, 5], 'day2': [2, 4, 6, 8, 10]})
  val = process_data(df['day2'], 'SQUARED')
  print(val)