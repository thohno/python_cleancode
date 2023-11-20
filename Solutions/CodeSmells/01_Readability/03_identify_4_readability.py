# Bad & redundant comments
# Bad variable/method naming
# Conditional complexity
# Temporary fields - "temp_result"

def calculate_sum_of_positive_values(data):
    """
    Calculate the sum of positive values in the given list.
    :param data: List of numbers
    :return: The sum of positive values in the list
    """
    positive_sum = 0
    for item in data:
        if item > 0:
            positive_sum += item
    return positive_sum


if __name__ == '__main__':
    pass