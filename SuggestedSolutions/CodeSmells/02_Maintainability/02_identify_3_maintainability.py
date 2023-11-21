# Magic strings/numbers
# Dead code
# High coupling/low cohesion to a library

# Reduce coupling to ExternalStore library and refactor to a Shopping service instead that houses both online & instore methods.
class GroceryShop:
    def __init__(self, shopping_service):
        self.shopping_service = shopping_service

    def buy_item(self, item, method):
        result = self.shopping_service.buy(item, method)
        print(f"Bought {item} using {method}. Result: {result}")

class ShoppingService:
    ONLINE_METHOD = "online"
    IN_STORE_METHOD = "in_store"
    def buy(self, item, method):
        if method == self.ONLINE_METHOD or method == self.IN_STORE_METHOD:
            # Common shopping logic for both online and in-store
            return f"{method.capitalize()} receipt for {item}"
        else:
            raise ValueError(f"Invalid method '{method}' for shopping.")


if __name__ == '__main__':
    pass