from enums import SpotType, VehicleType

class ParkingLot:
    def __init__(self, floors):
        self.floors = floors
        self.spots = {}

    def add_spot(self, floor, spot):
        if floor not in self.spots:
            self.spots[floor] = []
        self.spots[floor].append(spot)

    def find_available_spot(self, vehicle_type, has_handicapped_permit=False):
        for floor in self.spots:
            for spot in self.spots[floor]:
                if spot.is_available() and spot.can_fit_vehicle(vehicle_type, has_handicapped_permit):
                    return spot
        return None