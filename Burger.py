from Item import Item

TOPPINGS = {
    "Vegetables": [
        ("Lettuce", 0.0),
        ("Tomato", 0.0),
        ("Onion", 0.0),
        ("Pickles", 0.0)
    ],
    "Cheese": [
        ("Cheddar", 1.0),
        ("Gouda", 1.0)
    ],
    "Meat": [
        ("Bacon", 1.5),
        ("Ham", 1.5)
    ],
    "Special": [
        ("Avocado", 1.0),
        ("Jalapeños", 1.0)
    ]
}





class Burger:


    def __init__(self, name, price):
        if name == "Regular":
            self.name = name
            self.price = 4.0
        elif name == "Deluxe":
            self.name = name
            self.price = 8.5

        self.extras = []



    def add_topping(self,topping_name):
        topping_count = len(self.extras)
        for category, items in TOPPINGS.items():
            for topping, price in items:
                if topping == topping_name and self.name == "Regular":
                    self.extras.append(Item(type="topping",name=topping,price=price))
                elif topping == topping_name and self.name == "Deluxe" and topping_count <=4:
                    self.extras.append(Item(type="topping",name=topping,price=0))
                    topping_count +=1
                elif topping == topping_name and self.name == "Deluxe" and topping_count > 4:
                    self.extras.append(Item(type="topping", name=topping, price=price))


        if len(self.extras) < 1:
            raise ValueError("We don't have this topping!")

    def get_adjusted_price(self):
        total_price = self.price
        for topping in self.extras:
            total_price += topping.price

        return total_price

    def get_type(self):
        return self.name

    def get_topping_price(self, topping_name, number):
        for category, items in TOPPINGS.items():
            for topping, price in items:
                if topping.lower() == topping_name.lower() and self.name == "Deluxe" and number < 5:
                    return f"{0.00:.2f}"  # Returnăm prețul formatat cu 2 zecimale
                elif topping.lower() == topping_name.lower() and self.name == "Deluxe" and number == 5:
                    return f"{price:.2f}"  # Returnăm prețul formatat cu 2 zecimale
                elif topping.lower() == topping_name.lower():
                    return f"{price:.2f}"  # Returnăm prețul formatat cu 2 zecimale
        raise ValueError(f"Topping '{topping_name}' not found!")



    def print_itemized_list(self):
        print(f"Base {self.get_name()}: ${self.price:.2f}")
        for topping in self.extras:
            print(f"{topping.get_name()}: ${topping.get_adjusted_price():.2f}")



    def get_name(self):
        return f"{self.name} BURGER"
