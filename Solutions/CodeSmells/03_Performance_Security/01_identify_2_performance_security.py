# Lists instead of numpy arrays
# Generic exception handling

import numpy as np
def process_data(data):
    try:
        result = np.array(data) * 2
    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
        result = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        result = None
    return result


if __name__ == '__main__':
    pass