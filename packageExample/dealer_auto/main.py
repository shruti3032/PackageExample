from dealer_auto import InventoryManager, SalesProcessor, Notifier

# Initialize modules
inventory = InventoryManager()
sales = SalesProcessor(inventory)
notifier = Notifier()

# Add cars to inventory
inventory.add_car("1HGCM82633A123456", "Honda", "Civic", 22000)
inventory.add_car("5YJ3E1EA7KF317456", "Tesla", "Model 3", 35000)

# Display inventory
print("\nAvailable Cars:", inventory.list_cars())

# Sell a car
sold_car = sales.sell_car("1HGCM82633A123456", "John Doe")

# Notify customer
if sold_car:
    notifier.send_email("johndoe@example.com", f"Thank you for purchasing {sold_car['make']} {sold_car['model']}!")
    notifier.send_sms("+1234567890", f"Your {sold_car['make']} {sold_car['model']} purchase is confirmed!")
