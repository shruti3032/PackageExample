class InventoryManager:
    def __init__(self):
        self.cars = []  # List of available cars

    def add_car(self, vin, make, model, price):
        """Add a new car to inventory"""
        self.cars.append({"vin": vin, "make": make, "model": model, "price": price})
        print(f"Added {make} {model} to inventory.")

    def list_cars(self):
        """List all cars in inventory"""
        return self.cars
