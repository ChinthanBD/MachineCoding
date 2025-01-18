from vehicle import Vehicle
class SecuritySystem:
    def __init__(self):
        self.cameras = []

    def add_camera(self, camera: str) -> None:
        self.cameras.append(camera)

    def track_entry_exit(self, vehicle: Vehicle) -> None:
        print(f"Tracking entry/exit for vehicle: {vehicle.license_plate}")


