

from payment import PaymentSystem
from parking_lot import ParkingLot, SpotType
from parking_spot import ParkingSpot
from vehicle import Vehicle, VehicleType 
from security import SecuritySystem
from user_interface import UserInterface
from notifications import NotificationSystem
from enums import SpotType, VehicleType

if __name__ == "__main__":
    # Create a parking lot with 3 floors
    parking_lot = ParkingLot(floors=3)

    # Add parking spots to the parking lot
    parking_lot.add_spot(floor=1, spot=ParkingSpot(spot_id="1A", spot_type=SpotType.REGULAR))
    parking_lot.add_spot(floor=1, spot=ParkingSpot(spot_id="1B", spot_type=SpotType.COMPACT))
    parking_lot.add_spot(floor=2, spot=ParkingSpot(spot_id="2A", spot_type=SpotType.HANDICAPPED))

    # Create vehicles
    car = Vehicle(license_plate="ABC123", vehicle_type=VehicleType.CAR)
    motorcycle = Vehicle(license_plate="XYZ789", vehicle_type=VehicleType.MOTORCYCLE)
    handicapped_car = Vehicle(license_plate="HANDI1", vehicle_type=VehicleType.CAR, has_handicapped_permit=True)

    # Find available spot for a car
    available_spot = parking_lot.find_available_spot(vehicle_type=VehicleType.CAR)
    if available_spot:
        print(f"Available spot for car: {available_spot.spot_id}")
        available_spot.reserve()
    else:
        print("No available spot for car")

    # Find available spot for a handicapped car
    available_spot = parking_lot.find_available_spot(vehicle_type=VehicleType.CAR, has_handicapped_permit=True)
    if available_spot:
        print(f"Available spot for handicapped car: {available_spot.spot_id}")
        available_spot.reserve()
    else:
        print("No available spot for handicapped car")

    # Process payment
    payment_system = PaymentSystem()
    fee = payment_system.calculate_fee(duration=2)  # Assume 2 hours of parking
    payment_system.process_payment(amount=fee, method="credit card")

    # Track entry and exit
    security_system = SecuritySystem()
    security_system.track_entry_exit(vehicle=car)

    # Display available spots through UI
    ui = UserInterface(parking_lot=parking_lot)
    ui.display_available_spots()

    # Send notification
    notification_system = NotificationSystem()
    notification_system.send_notification(message="Your parking time is about to expire")

# Expected output:
# Available spot for car: 1A
# Available spot for handicapped car: 2A
# Processing payment of 20 using credit card
# Tracking entry/exit for vehicle: ABC123
# Floor 1 - Spot 1B is available
# Notification: Your parking time is about to expire