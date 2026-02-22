# Step 1: Define the ItemToPurchase class with appropriate attributes and methods
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:g} = ${total_cost:g}")
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


# Step 2: Create two instances of ItemToPurchase and gather user input       
if __name__ == "__main__":
    
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    
    print("Item 1")
    item1.item_name = input("Enter the item name: ")
    item1.item_price = float(input("Enter the item price: "))
    item1.item_quantity = int(input("Enter the item quantity: "))
    
    print("\nItem 2")
    item2.item_name = input("Enter the item name: ")
    item2.item_price = float(input("Enter the item price: "))
    item2.item_quantity = int(input("Enter the item quantity: "))
    
    # Step 3: Print the total cost for each item and the overall total
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"Total: ${total:g}")

    

