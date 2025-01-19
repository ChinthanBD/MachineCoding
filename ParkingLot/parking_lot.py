from enums import SpotType, VehicleType
from abc import ABC, abstractmethod
    
class SpotFindingStrategy(ABC):
    
    @abstractmethod
    def find_spot(self, spots, vehicle_type, has_handicapped_permit):
        pass
    

class NearestSpotFindingStrategy(SpotFindingStrategy):
    def find_spot(self, spots, vehicle_type, has_handicapped_permit):
        for floor in sorted(spots.keys()):
            for spot in sorted(spots[floor], key=lambda x: x.spot_id):
                if spot.is_available() and spot.can_fit_vehicle(vehicle_type, has_handicapped_permit):
                    return spot
        return None

class HandicappedSpotFindingStrategy(SpotFindingStrategy):
    def find_spot(self, spots, vehicle_type, has_handicapped_permit):
        for floor in spots:
            for spot in spots[floor]:
                if spot.is_available() and spot.is_handicapped() and spot.can_fit_vehicle(vehicle_type, has_handicapped_permit):
                    return spot
        return None

class ParkingLot:
    def __init__(self, floors):
        self.floors = floors
        self.spots = {}

    def add_spot(self, floor, spot):
        if floor not in self.spots:
            self.spots[floor] = []
        self.spots[floor].append(spot)

    def find_available_spot(self, vehicle_type, has_handicapped_permit=False):
        return self.strategy.find_spot(self.spots, vehicle_type, has_handicapped_permit)
    

    def find_available_spot(self, vehicle_type, has_handicapped_permit=False):
        if has_handicapped_permit:
            strategy = HandicappedSpotFindingStrategy()
        else:
            strategy = NearestSpotFindingStrategy()
        return strategy.find_spot(self.spots, vehicle_type, has_handicapped_permit)