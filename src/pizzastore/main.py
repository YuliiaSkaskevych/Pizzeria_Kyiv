from information.pizzas_info import pizzas_items
from items.receiptline import ReceiptLine
from items.pizza import Pizza
from collections import deque
import itertools
import random

pizzas = [Pizza(idx, name, price, description) for idx, name, price, description in pizzas_items]

def greetings():
    print("Welcome to the best pizzeria in Kyiv - ARSENAL!")
    print("To view the menu - enter 1")
    print("Exit - 0")
    print("To see pizzas that cost more than 150 -enter 2", "To see the queue - enter 3", sep="\n")


def decorator(func):
    def inner(l):
        a = "*"*40
        print(a)
        func(l)
        print(f"Total: {len(l)}")
        print(a)
    return inner

@decorator
def print_menu(l):
    for element in l:
        print(f"Pizza:{element.name} Price:{element.price}")
        print(f"Description of pizza:{element.description}")

def print_filter(n, a):
    for element in n:
        if element.price > a:
            print(f"Pizza:{element.name} Price:{element.price}")

def deque_tables():
    q = deque([random.randint(1, 9) for i in range(20)])
    print("Numbers of tables in queue:", q)
    while len(q):
        a = random.sample(pizzas, random.randint(1, 11))
        print(f"Table №{q.popleft(), [element.name for element in a]}")
    print("No orders")


while True:
    greetings()
    menu=input("Please, enter the number: ")
    match menu:
        case "0":
            print("Good luck!")
            break
        case "1":
            print("You can see our menu:")
            print_menu(pizzas)
        case "2":
            print_filter(pizzas, 150)
        case "3":
            deque_tables()
        case _:
            print("Wrong input")
            print("Please, try again!")