# Identify the 2 code smells from the following list:
# Lists instead of numpy arrays
# For loops instead of vectorized operations
# Access credentials in the code
# Unsanitized queries
# Generic exception handling

def process_data(data):
    try:
        result = []
        for item in data:
            processed_item = item * 2
            result.append(processed_item)
    except Exception as e:
        print(f"An error occurred: {e}")
        result = None
    return result


if __name__ == '__main__':
    pass