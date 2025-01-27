from abc import ABC
from collections import defaultdict

class Vehicle(ABC):
    def __init__(self, licence_plate: str, size: int):
        self.licence_plate = licence_plate
        self.size = size

    def get_size(self):
        return self.size

    def __repr__(self):
        return f"Vehicle with licence plate: {self.licence_plate}"


class Car(Vehicle):
    def __init__(self, licence_plate: str):
        super().__init__(licence_plate, 1)


class Limo(Vehicle):
    def __init__(self, licence_plate: str):
        super().__init__(licence_plate, 2)


class SemiTruck(Vehicle):
    def __init__(self, licence_plate: str):
        super().__init__(licence_plate, 3)


class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_available = True
        self.vehicle = None

    def park(self, vehicle):
        if not self.is_available:
            raise Exception("Parking spot not available")

        self.is_available = False
        self.vehicle = vehicle

    def free(self):
        if self.is_available:
            raise Exception("Parking spot is already available")

        self.is_available = True
        self.vehicle = None

    def __repr__(self):
        if self.is_available:
            return f"Spot ({self.spot_id}), is available"
        else:
            return f"Spot ({self.spot_id}), occupied by {self.vehicle}"


class ParkingLevel:
    def __init__(self, level_id, num_spots):
        self.level_id = level_id
        self.spots = [ParkingSpot(i) for i in range(num_spots)]
        self.vehicle_to_spots = defaultdict(list)

    def park_vehicle(self, vehicle):
        available_spots = []
        for spot in self.spots:
            if spot.is_available:
                available_spots.append(spot)
                if len(available_spots) == vehicle.get_size():
                    for spot in available_spots:
                        spot.park(vehicle)
                    self.vehicle_to_spots[vehicle].extend(available_spots)
                    return True

            # Reset available spots, as we need contiguous spots for a vehicle
            if not spot.is_available:
                available_spots = []

        return False

    def free_vehicle(self, vehicle):
        if vehicle not in self.vehicle_to_spots:
            raise Exception("Vehicle not present at level")
        for spot in self.vehicle_to_spots[vehicle]:
            spot.free()
        del self.vehicle_to_spots[vehicle]

    def __repr__(self):
        val = f"Level {self.level_id}. Total spots: {len(self.spots)}"
        for spot in self.spots:
            val += f"\n\t{spot}"
        return val


class ParkingLot:
    def __init__(self, num_levels, spots_per_level):
        self.levels = [ParkingLevel(i, spots_per_level) for i in range(num_levels)]
        self.level_to_vehicle = defaultdict()

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                self.level_to_vehicle[vehicle] = level
                print(f"{vehicle} parked at level {level.level_id}")
                return True

        print(f"{vehicle} can't be parked. All levels are full")

    def free_vehicle(self, vehicle):
        if vehicle not in self.level_to_vehicle:
            raise Exception(f"The {vehicle} not parked at the parking lot!!")

        level = self.level_to_vehicle[vehicle]
        level.free_vehicle(vehicle)
        del self.level_to_vehicle[vehicle]
        print(f"{vehicle} freed at {level.level_id}")

    def __repr__(self):
        val = ''
        for level in self.levels:
            val += f'\n{level}'
        return val


if __name__ == "__main__":
    parking_lot = ParkingLot(3, 5)
    print(parking_lot)

    car = Car("CAR123")
    parking_lot.park_vehicle(car)

    limo = Limo("LIMO123")
    parking_lot.park_vehicle(limo)

    truck = SemiTruck("TRUCK123")
    parking_lot.park_vehicle(truck)

    truck = SemiTruck("TRUCK456")
    parking_lot.park_vehicle(truck)

    truck = SemiTruck("TRUCK798")
    parking_lot.park_vehicle(truck)

    print(parking_lot)
