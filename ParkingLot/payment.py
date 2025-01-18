class PaymentSystem:
    def calculate_fee(self, duration: int) -> int:
        rate_per_hour = 10  # Example rate
        return duration * rate_per_hour

    def process_payment(self, amount: int, method: str) -> None:
        print(f"Processing payment of {amount} using {method}")
