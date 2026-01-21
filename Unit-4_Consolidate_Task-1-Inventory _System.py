import csv
import os

INVENTORY_FILE = "inventory.csv"

# Inventory structure: {product_name: {"quantity": int, "price": float}}
inventory = {}

# --- File Handling Functions ---
def load_inventory():
    
    if not os.path.exists(INVENTORY_FILE):
        return
    with open(INVENTORY_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        for row in reader:
            if len(row) == 3:
                name, qty, price = row
                inventory[name] = {"quantity": int(qty), "price": float(price)}

def save_inventory():
   
    with open(INVENTORY_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Quantity", "Price"])
        for name, data in inventory.items():
            writer.writerow([name, data["quantity"], data["price"]])


def add_product():
    name = input("Enter product name: ").strip()
    if name in inventory:
        print("Product already exists! Use 'update product' instead.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"{name} added successfully!")
    except ValueError:
        print("Invalid input. Quantity must be an integer and price must be a number.")

def update_product():
    name = input("Enter product name to update: ").strip()
    if name not in inventory:
        print("Product not found!")
        return
    print(f"Current details: {inventory[name]}")
    try:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        inventory[name]["quantity"] = quantity
        inventory[name]["price"] = price
        print(f"{name} updated successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- Current Inventory ---")
    print(f"{'Product Name':<20} {'Quantity':<10} {'Price':<10}")
    print("-" * 45)
    for name, data in inventory.items():
        print(f"{name:<20} {data['quantity']:<10} {data['price']:<10.2f}")
    print("-" * 45)


def main():
    load_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Display Inventory")
        print("4. Save & Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            save_inventory()
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1-4.")

if __name__ == "__main__":
    main()
    

    
