# Duplicate code
# Magic strings/numbers
# High coupling/low cohesion

class PaymentProcessor:
    FEE_RATES = {"credit_card": 0.02,
                 "paypal": 0.05,
                 "bank_transfer": 0.01,
                 "stripe": 0.03}
    def process_payment(self, amount, method):
        fee = self.calculate_fee(amount, method)
        print(f"Processing {method} payment with fee: {fee}")

    def calculate_fee(self, amount, method):
        return amount * self.FEE_RATES.get(method, 0)


if __name__ == '__main__':
    pass