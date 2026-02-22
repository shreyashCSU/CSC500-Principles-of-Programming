from ItemToPurchase import ItemToPurchase


class ShoppingCart:
    """Represents a customer's shopping cart."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        for idx, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item_name:
                del self.cart_items[idx]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item: ItemToPurchase):
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
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
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
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart: ShoppingCart):
    # Step 5: Build and display menu options until user quits.
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
            # Step 5 scope: menu option exists; implementation completed in later milestones.
            continue
        elif choice == "r":
            # Step 5 scope: menu option exists; implementation completed in later milestones.
            continue
        elif choice == "c":
            # Step 5 scope: menu option exists; implementation completed in later milestones.
            continue
        elif choice == "i":
            # Step 6: Output item descriptions.
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            # Step 6: Output shopping cart total view.
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == "q":
            break
        else:
            # Invalid choice: keep prompting until a valid option is entered.
            continue


def main():
    # Step 5: Call print_menu() from main.
    cart = ShoppingCart()
    print_menu(cart)


if __name__ == "__main__":
    main()

