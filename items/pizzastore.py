import random
import csv
from collections import deque
from items.pizza import Pizza
from items.receipt import Receipt
from items.table import Table



read_pizza = open("src\pizzastore\information\pizzas_info", "r")
pizza_info = csv.reader(read_pizza, delimiter=",", quoting=csv.QUOTE_MINIMAL)

read_table = open("src\pizzastore\information\info_tables", "r")
tables_info = csv.reader(read_table, delimiter=",", quoting=csv.QUOTE_MINIMAL)


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def decorator(method):
    def inner(x, b):
        a = "*"*40
        print(a)
        method(x, b)
        print(f"Total: {len(b)}")
        print(a)
    return inner


class PizzaStore(metaclass=SingletonMeta):
    def __init__(self):
        self.pizzas = [Pizza(int(i[0]),i[1],int(i[2]),i[3]) for i in pizza_info]
        self.table = [Table(int(i[0]),i[1],i[2]) for i in tables_info]
        self.receipts = []

    def print_receipts(self):
        for i in self.receipts:
            print(i)

    def print_last(self):
        for i in self.receipts:
            print(self.receipts[-1])
            break


    def add_receipt(self, r_item: Receipt):
        self.receipts.append(r_item)

    def greetings(self):
        print("Welcome to the best pizzeria in Kyiv - ARSENAL!")
        print("To view the menu - enter 1")
        print("Exit - 0")
        print("To see pizzas that cost more than you want -enter 2", "To see the receipt - enter 3",
              "To see the deque of tables - enter 4", "To editor receipt - enter 5" , sep="\n")

    def editor(self):
        print("To change count of pizza (more or less) - enter 1",
              "To enter count of pizza - enter 2",
              "Delete pizza in receipt - enter 3", sep="\n")

    @decorator
    def print_menu(self, pizzas):
        print("You can see our menu: ")
        for element in pizzas:
            print("-"*40)
            print(f"Pizza:{element.name} Price:{element.price}")
            print(f"Description of pizza:{element.description}")

    def get_table(self):
        return random.choice(self.table)

    def deque_tables(self):
        q = deque([random.choice(self.table) for i in range(random.randint(5, 20))])
        x = [el.name for el in self.pizzas]
        print(f"Deque of tables: {len(q)}")
        while len(q):
            print(f"{q.popleft()} → ")
            print(*random.sample(x, random.randint(1, 5)))
        print("No orders")

















