# Bad & redundant comments
# Bad variable/method naming
# Cyclomatic complexity

# first improve bad naming & comments
def calculate(num_list, n):
    result = 0
    i = 0
    while i < n:
        if num_list[i] % 2 == 0:
            result += num_list[i]
        i += 1
    return result

# improving cyclomatic complexity
def sum_even_numbers(num_list):
    result = 0
    for num in num_list:
        if num % 2 == 0:
            result += num
    return result


if __name__ == '__main__':
    pass