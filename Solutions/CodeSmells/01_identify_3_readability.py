# Too many function arguments
# Deeply nested control flow
# Side effects

def process_item(item, threshold, divisor, multiplier):
    if not is_valid_item(item, threshold, divisor):
        print("Item is invalid")
        return
    result = item * multiplier
    print("Processing completed.")
    return result


def is_valid_item(item, threshold, divisor):
    return item > threshold and item % divisor == 0


if __name__ == '__main__':
    pass