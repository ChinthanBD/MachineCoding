from enum import Enum

# Enum for vehicle types
class VehicleType(Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"

# Enum for spot types
class SpotType(Enum):
    REGULAR = "regular"
    COMPACT = "compact"
    HANDICAPPED = "handicapped"