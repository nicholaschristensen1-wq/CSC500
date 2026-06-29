"""
CSC500 - CT4: Online Shopping Cart (Portfolio Milestone, Week 4)
ItemToPurchase class + two-item driver program.
Python 3.14.5
"""


class ItemToPurchase:
    """Represents a single item that may be added to a shopping cart."""

    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        """Print the item line in the assignment's required format."""
        line_total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ "
              f"${self.item_price} = ${line_total}")


def prompt_item(label):
    """Prompt the user for one item's data and return a populated object."""
    print(f"\nItem {label}")
    print("Enter the item name:")
    name = input()
    print("Enter the item price:")
    price = float(input())
    print("Enter the item quantity:")
    quantity = int(input())
    return ItemToPurchase(name, price, quantity)


def main():
    print("Online Shopping Cart")
    print("--------------------")

    item_1 = prompt_item("1")
    item_2 = prompt_item("2")

    total = (item_1.item_price * item_1.item_quantity) + \
            (item_2.item_price * item_2.item_quantity)

    print("\nTOTAL COST")
    item_1.print_item_cost()
    item_2.print_item_cost()
    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
