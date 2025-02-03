class SalesProcessor:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager

    def sell_car(self, vin, customer_name):
        """Process a car sale"""
        for car in self.inventory.cars:
            if car["vin"] == vin:
                self.inventory.cars.remove(car)
                print(f"Sold {car['make']} {car['model']} to {customer_name}.")
                return car
        print("Car not found in inventory.")
        return None
