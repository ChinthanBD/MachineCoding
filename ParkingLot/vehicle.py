from enums import VehicleType

class Vehicle:
    def __init__(self, license_plate, vehicle_type, has_handicapped_permit=False):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.has_handicapped_permit = has_handicapped_permit