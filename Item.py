class Item:
    VALID_TYPE = ["burger","drink","side","topping"]

    def __init__(self,type,name,price,size = "MEDIUM"):
        if type.lower() not in self.VALID_TYPE:
            raise ValueError(f"Invalid type: {type}. Valid types are: {', '.join(self.VALID_TYPE)}")

        self.type = type.lower()
        self.name = name.capitalize()
        self.price = price
        self.size = size.upper()

        if self.type in ["drink", "side"] and self.size not in ["SMALL", "MEDIUM", "LARGE"]:
            raise ValueError("Invalid size. Size must be SMALL, MEDIUM, or LARGE for drinks and sides.")

    def get_name(self):
        if self.type in ["drink", "side"]:
            return f"{self.size} {self.name}"
        return self.name

    def get_base_price(self):
        return self.price

    def get_adjusted_price(self):
        pret = self.price
        if self.size == "SMALL":
            pret = self.price - 0.5
        elif self.size == "LARGE":
            pret = self.price + 1

        return pret

    def set_size(self, x):
        x = x.upper()
        if x not in ["SMALL", "MEDIUM", "LARGE"]:
            raise ValueError("Invalid size. Size must be SMALL, MEDIUM, or LARGE.")
        self.size = x