from ItemToPurchase import ItemToPurchase


class ShoppingCart:
    """Represents a customer's shopping cart and related operations."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item: ItemToPurchase):
        # Adds a new ItemToPurchase object to the cart.
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        # Removes the first matching item by name.
        for idx, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item_name:
                del self.cart_items[idx]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item: ItemToPurchase):
        # Updates an existing item; only non-default input values are applied.
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Returns the sum of quantities across all items.
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        # Returns the total dollar cost for all cart items.
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        # Prints cart header, each line item cost, and the total.
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if self.get_num_items_in_cart() == 0:
            print("\nSHOPPING CART IS EMPTY")
            print("Total: $0")
            return

        print()
        for item in self.cart_items:
            item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():g}")

    def print_descriptions(self):
        # Prints all item descriptions in the cart.
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart: ShoppingCart):
    # Displays menu options and processes user actions until quit.
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit"
    )

    choice = ""
    while choice != "q":
        print(menu)
        choice = input("Choose an option:\n").strip().lower()

        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, quantity, description))
        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=quantity))
        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == "q":
            break
        else:
            # Invalid choice: keep prompting until a valid option is entered.
            continue


def main():
    # Entry point for Milestone 2 + final project requirements.
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
