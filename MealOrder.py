from Burger import Burger
from Item import Item


class MealOrder:

    def __init__(self, burger_type="Regular", drink_type="Coke", side_type="Fries"):
        # Inițializare burger
        self.burger = Burger(burger_type, 4.0 if burger_type.lower() != "deluxe" else 8.5)

        # Inițializare băutură
        self.drink = Item(type="drink", name=drink_type, price=1.0)

        # Inițializare garnitură
        self.side = Item(type="side", name=side_type, price=1.5)

    def get_total_price(self):
        return (
            self.burger.get_adjusted_price() +
            self.drink.get_adjusted_price() +
            self.side.get_adjusted_price()
        )

    def add_burger_toppings(self, *toppings):
        for topping in toppings:
            self.burger.add_topping(topping)

    def set_drink_size(self, size):
        self.drink.set_size(size)

    def set_side_size(self, size):
        self.side.set_size(size)

    def print_itemized_list(self):
        print("Your Order:")
        print("-" * 30)
        self.burger.print_itemized_list()
        print(f"{self.drink.get_name()}: ${self.drink.get_adjusted_price():.2f}")
        print(f"{self.side.get_name()}: ${self.side.get_adjusted_price():.2f}")
        print("-" * 30)
        print(f"Total: ${self.get_total_price():.2f}")


# Creăm o comandă
order = MealOrder(burger_type="Regular", drink_type="Coke", side_type="Fries")

# Adăugăm toppinguri la burger
order.add_burger_toppings("Bacon", "Cheddar", "Lettuce")

# Setăm dimensiunea băuturii și garniturii
order.set_drink_size("LARGE")
order.set_side_size("SMALL")

# Afișăm lista detaliată
order.print_itemized_list()
