from Burger import Burger
from Item import Item


class DeluxeBurger(Burger):
    def __init__(self, name="Deluxe", price=8.5):
        super().__init__(name, price)

        self.deluxe_toppings = [
            Item(type="topping", name="Chips", price=0.0),
            Item(type="topping", name="Drink", price=0.0)
        ]

    def add_topping(self, topping_name):

        if len(self.extras) >= 3:
            raise ValueError("You can only add up to 3 additional toppings.")
        super().add_topping(topping_name)

    def get_adjusted_price(self):

        total_price = super().get_adjusted_price()
        return total_price

    def print_itemized_list(self):

        print(f"Base {self.get_name()}: ${self.price:.2f}")


        for topping in self.deluxe_toppings:
            print(f"{topping.get_name()}: Included")


        for topping in self.extras:
            print(f"{topping.get_name()}: ${topping.get_adjusted_price():.2f}")

        print("-" * 30)
        print(f"Total: ${self.get_adjusted_price():.2f}")


