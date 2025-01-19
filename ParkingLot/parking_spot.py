from enums import SpotType, VehicleType

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False

    def is_available(self) -> bool:
        return not self.is_occupied

    def can_fit_vehicle(self, vehicle_type: VehicleType, has_handicapped_permit=False):
        if self.spot_type == SpotType.REGULAR and vehicle_type in [VehicleType.CAR, VehicleType.TRUCK]:
            return True
        elif self.spot_type == SpotType.COMPACT and vehicle_type == VehicleType.CAR:
            return True
        elif self.spot_type == SpotType.HANDICAPPED and vehicle_type in [VehicleType.CAR, VehicleType.TRUCK] and has_handicapped_permit:
            return True
        return False

    def reserve(self):
        self.is_occupied = True

    def release(self):
        self.is_occupied = False
    
    def is_handicapped(self) -> bool:
        return self.spot_type == SpotType.HANDICAPPED