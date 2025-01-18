from payment import PaymentSystem
from parking_lot import ParkingLot  # Assuming ParkingLot is defined in parking_lot module

# user_interface.py
class UserInterface:
    def __init__(self, parking_lot: ParkingLot):
        self.parking_lot = parking_lot

    def display_available_spots(self) -> None:
        for floor in self.parking_lot.spots:
            for spot in self.parking_lot.spots[floor]:
                if spot.is_available():
                    print(f"Floor {floor} - Spot {spot.spot_id} is available")

    def process_payment(self, amount: float, method: str) -> None:
        payment_system = PaymentSystem()
        payment_system.process_payment(amount, method)
