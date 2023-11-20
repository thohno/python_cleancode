# Identify the 3 code smells from the following list:
# Duplicate code
# Magic strings/numbers
# Dead code
# High coupling/low cohesion
# High coupling/low cohesion to a library

class PaypalPaymentProcessor:
    def process_payment(self, amount, method):
        if method == "credit_card":
            fee = self.calculate_credit_card_fee(amount)
            print(f"Processing credit card payment with fee: {fee}")
        elif method == "bank_transfer":
            fee = self.calculate_bank_transfer_fee(amount)
            print(f"Processing bank transfer payment with fee: {fee}")
        else:
            fee = amount * 0.05
            print(f"Processing PayPal payment with fee: {fee}")

    class StripePaymentProcessor:
        def process_payment(self, amount, method):
            if method == "credit_card":
                fee = self.calculate_credit_card_fee(amount)
                print(f"Processing credit card payment with fee: {fee}")
            elif method == "bank_transfer":
                fee = self.calculate_bank_transfer_fee(amount)
                print(f"Processing bank transfer payment with fee: {fee}")
            else:
                fee = amount * 0.03
                print(f"Processing Stripe payment with fee: {fee}")


if __name__ == '__main__':
    pass