class ParkingLot:
    def __init__(self):
        self.level_a = {i: None for i in range(1, 21)}
        self.level_b = {i: None for i in range(21, 41)}
        self.parked_vehicles = {}  # {vehicle_number: (level, spot)}

    def assign_parking_space(self, vehicle_number):
        for level, spots in [("A", self.level_a), ("B", self.level_b)]:
            for spot, status in spots.items():
                if status is None:
                    spots[spot] = vehicle_number
                    self.parked_vehicles[vehicle_number] = (level, spot)
                    return {"level": level, "spot": spot}

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            level, spot = self.parked_vehicles[vehicle_number]
            return {"level": level, "spot": spot}
        else:
            return {"error": "Vehicle not found in the parking lot."}

    def unpark_vehicle(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            level, spot = self.parked_vehicles[vehicle_number]
            self.parked_vehicles.pop(vehicle_number)
            if level == "A":
                self.level_a[spot] = None
            else:
                self.level_b[spot] = None
            return {"message": "Vehicle unparked successfully."}
        else:
            return {"error": "Vehicle not found in the parking lot."}


# Example Usage
if __name__ == "__main__":
    parking_lot = ParkingLot()

    # Assign parking space to a new vehicle
    result = parking_lot.assign_parking_space("ABC123")
    print(result)  # Output: {'level': 'A', 'spot': 1}

    # Retrieve parking spot number of a particular vehicle
    result = parking_lot.retrieve_parking_spot("ABC123")
    print(result)  # Output: {'level': 'A', 'spot': 1}

    # # Unpark the vehicle
    # result = parking_lot.unpark_vehicle("ABC123")
    # print(result)  # Output: {'message': 'Vehicle unparked successfully.'}


    print(parking_lot.assign_parking_space("ABC1234"))
    print(parking_lot.assign_parking_space("ABC12345"))
    print(parking_lot.retrieve_parking_spot("ABC1234"))
    print(parking_lot.unpark_vehicle("ABC1234"))
    print(parking_lot.assign_parking_space("ABC123456"))

    print(parking_lot.retrieve_parking_spot("ABC123"))
    print(parking_lot.retrieve_parking_spot("ABC1234"))
    print(parking_lot.retrieve_parking_spot("ABC12345"))
    print(parking_lot.retrieve_parking_spot("ABC123456"))