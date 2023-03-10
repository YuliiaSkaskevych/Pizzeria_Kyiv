
from items.pizza import Pizza

class ReceiptLine:
    def __init__(self, pizza: Pizza, num: int):
        self.pizza = pizza
        self.num = num

    def __str__(self):
        return f"{self.pizza.name:<15} * {self.num:<3} = {self.pizza.get_price()*self.num:^5} UAN "

    def change_number_pizzas(self, n: int):
        if (n>0):
            self.num += n
        elif (n<0) and n + self.num >= 0:
            self.num -= abs(n)
        else:
            self.num += 0

    def amount_pizzas(self, n: int):
        if (n>0):
            self.num = n
        else:
            print("Error input")












