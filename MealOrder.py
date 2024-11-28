from Burger import *
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

    def get_burger_type(self):
        return self.burger.get_type()

    def add_burger_toppings(self, *toppings):
        for topping_list in toppings:
            if isinstance(topping_list, list):  # Verificăm dacă este o listă
                for topping in topping_list:
                    self.burger.add_topping(topping)  # Adăugăm fiecare topping individual

            else:
                self.burger.add_topping(topping_list)  # Dacă este un singur element, îl adăugăm direct





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

    def get_burger_price(self):
        return self.burger.get_adjusted_price()




# order = MealOrder("Deluxe","Coke","Fries")
# order.set_side_size("MEDIUM")
# order.set_drink_size("MEDIUM")
# order.add_burger_toppings("Cheddar", "Gouda","Bacon","Ham","Avocado","Jalapeños")
# print(order.get_total_price())
# order.print_itemized_list()
#
