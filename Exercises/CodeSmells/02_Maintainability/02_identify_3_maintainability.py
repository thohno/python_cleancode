# Identify the 3 code smells from the following list:
# Duplicate code
# Magic strings/numbers
# Dead code
# High coupling/low cohesion
# High coupling/low cohesion to a library

class GroceryShop:
    def buy_item(self, item, method):
        external_store = ExternalStore()
        if method == "online":
            result = external_store.buy_online(item)
            print(f"Bought {item} online. Result: {result}")
        elif method == "in_store":
            result = external_store.buy_in_store(item)
            print(f"Bought {item} in-store. Result: {result}")

        # temporarily not in use due to requirements
        # def print_receipt(self):
        #     print("Printing receipt...")

class ExternalStore:
    def buy_online(self, item):
    # Online shopping logic
        return f"Online receipt for {item}"

    def buy_in_store(self, item):
    # In-store shopping logic
        return f"In-store receipt for {item}"


if __name__ == '__main__':
    pass