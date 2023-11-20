# Identify the 4 code smells from the following list:
# Long methods
# Bad & redundant comments
# Bad variable/method naming
# Too many function arguments
# Conditional complexity
# Deeply nested control flow
# Cyclomatic complexity
# Temporary fields
# Side effects

def process_data(data):
    # Check if data is valid
    if data:
        temp_result = 0
        for item in data:
        # Calculate the item's value
            if item > 0:
                temp_result += item
            # Skip negative values
            else:
                pass
            return temp_result
    else:
        return 0


if __name__ == '__main__':
    pass