# Identify the 3 code smells from the following list:
# Long methods
# Bad & redundant comments
# Bad variable/method naming
# Too many function arguments
# Conditional complexity
# Deeply nested control flow
# Cyclomatic complexity
# Temporary fields
# Side effects

def process_item(item, threshold, divisor, multiplier, accumulator):
    if item > threshold:
        if item % divisor == 0:
            if item < threshold * 2:
                result = item * multiplier
                accumulator += result
                print("Processing completed")
            else:
                print("Item value too large")
        else:
            print("Item is not divisible by the divisor")
    else:
        print("Item is not greater than the threshold")


if __name__ == '__main__':
    pass