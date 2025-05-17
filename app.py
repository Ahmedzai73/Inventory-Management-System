from datetime import datetime

# Product class - basic product information
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def show_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Price: Rs{self.price}, Quantity: {self.quantity}")

# Electronics class - inherits from Product
class Electronics(Product):
    def __init__(self, id, name, price, quantity, brand, warranty):
        super().__init__(id, name, price, quantity)
        self.brand = brand
        self.warranty = warranty
    
    def show_info(self):
        print(f"[Electronics] ID: {self.id}, Name: {self.name}, Brand: {self.brand}, Price: Rs{self.price}, Quantity: {self.quantity}, Warranty: {self.warranty} years")

# Grocery class - inherits from Product
class Grocery(Product):
    def __init__(self, id, name, price, quantity, expiry_date):
        super().__init__(id, name, price, quantity)
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
    
    def is_expired(self):
        return self.expiry_date < datetime.now()
    
    def show_info(self):
        status = "Expired" if self.is_expired() else "Good"
        print(f"[Grocery] ID: {self.id}, Name: {self.name}, Price: Rs{self.price}, Quantity: {self.quantity}, Expiry: {self.expiry_date.date()} ({status})")

# Clothing class - inherits from Product
class Clothing(Product):
    def __init__(self, id, name, price, quantity, size, material):
        super().__init__(id, name, price, quantity)
        self.size = size
        self.material = material
    
    def show_info(self):
        print(f"[Clothing] ID: {self.id}, Name: {self.name}, Price: Rs{self.price}, Quantity: {self.quantity}, Size: {self.size}, Material: {self.material}")

# Inventory system
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to inventory!")
    
    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                print(f"Removed {product.name} from inventory!")
                return
        print("Product not found!")
    
    def list_products(self):
        if not self.products:
            print("Inventory is empty!")
        else:
            print("\n--- ALL PRODUCTS ---")
            for product in self.products:
                product.show_info()
    
    def search_product(self, name):
        found = False
        for product in self.products:
            if name.lower() in product.name.lower():
                product.show_info()
                found = True
        if not found:
            print("No products found with that name!")
    
    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        print(f"Total inventory value: Rs{total:.2f}")
    
    def remove_expired(self):
        expired = []
        for product in self.products:
            if isinstance(product, Grocery) and product.is_expired():
                expired.append(product)
        
        for product in expired:
            self.products.remove(product)
            print(f"Removed expired product: {product.name}")
        
        if not expired:
            print("No expired products found!")

# Main program
def main():
    inventory = Inventory()
    
    while True:
        print("\n===== Inventory Management System =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. List All Products")
        print("4. Search Product")
        print("5. Calculate Total Value")
        print("6. Remove Expired Groceries")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nWhat type of product?")
            print("1. Electronics")
            print("2. Grocery")
            print("3. Clothing")
            type_choice = input("Enter type (1-3): ")
            
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            
            if type_choice == "1":
                brand = input("Enter brand: ")
                warranty = input("Enter warranty (years): ")
                product = Electronics(id, name, price, quantity, brand, warranty)
            elif type_choice == "2":
                expiry = input("Enter expiry date (YYYY-MM-DD): ")
                product = Grocery(id, name, price, quantity, expiry)
            elif type_choice == "3":
                size = input("Enter size: ")
                material = input("Enter material: ")
                product = Clothing(id, name, price, quantity, size, material)
            else:
                print("Invalid choice!")
                continue
            
            inventory.add_product(product)
        
        elif choice == "2":
            product_id = input("Enter product ID to remove: ")
            inventory.remove_product(product_id)
        
        elif choice == "3":
            inventory.list_products()
        
        elif choice == "4":
            name = input("Enter product name to search: ")
            inventory.search_product(name)
        
        elif choice == "5":
            inventory.total_value()
        
        elif choice == "6":
            inventory.remove_expired()
        
        elif choice == "0":
            print("Thank you for using Inventory Management System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()