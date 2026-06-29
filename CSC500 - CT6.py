"""
CSC500 - CT6: Online Shopping Cart Part 2 (Portfolio Milestone, Week 6)
ItemToPurchase + ShoppingCart classes with a menu-driven interface.
Python 3.14.5
"""


class ItemToPurchase:
    """A single item that can be placed in the shopping cart."""

    def __init__(self, item_name="none", item_price=0.0,
                 item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        line_total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ "
              f"${self.item_price} = ${line_total}")


class ShoppingCart:
    """A collection of ItemToPurchase objects belonging to one customer."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, name):
        for i, item in enumerate(self.cart_items):
            if item.item_name == name:
                del self.cart_items[i]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified):
        for item in self.cart_items:
            if item.item_name == modified.item_name:
                if modified.item_description != "none":
                    item.item_description = modified.item_description
                if modified.item_price != 0.0:
                    item.item_price = modified.item_price
                if modified.item_quantity != 0:
                    item.item_quantity = modified.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity
                   for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        print("-----------------")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


MENU = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit"""


def prompt_new_item():
    print("ADD ITEM TO CART")
    print("Enter the item name:")
    name = input()
    print("Enter the item description:")
    description = input()
    print("Enter the item price:")
    price = float(input())
    print("Enter the item quantity:")
    quantity = int(input())
    return ItemToPurchase(name, price, quantity, description)


def print_menu(cart):
    valid = {"a", "r", "c", "i", "o", "q"}
    while True:
        print(MENU)
        print("\nChoose an option:")
        choice = input().strip().lower()
        if choice == "q":
            return
        if choice not in valid:
            print("Invalid option. Please choose a, r, c, i, o, or q.")
            continue
        if choice == "a":
            cart.add_item(prompt_new_item())
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            cart.remove_item(input())
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            print("Enter the item name:")
            name = input()
            print("Enter the new quantity:")
            quantity = int(input())
            cart.modify_item(
                ItemToPurchase(item_name=name, item_quantity=quantity))
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()


def main():
    print("Enter customer's name:")
    name = input()
    print("Enter today's date:")
    date = input()
    cart = ShoppingCart(name, date)
    print(f"\nCustomer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")
    print_menu(cart)


if __name__ == "__main__":
    main()
