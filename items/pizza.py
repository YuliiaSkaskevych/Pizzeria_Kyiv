
class Pizza:
    def __init__(self, idx, name, price, description):
        self.idx = idx
        self.name = name
        self.price = price
        self.description = description

    def __str__ (self):
        return f"№{self.idx} Pizza: {self.name}, price: {self.price} UAN, description of pizza: {self.description}"

    def get_price(self):
        return self.price

    def get_desc(self):
        return f"Pizza {self.name} → {self.description}"


