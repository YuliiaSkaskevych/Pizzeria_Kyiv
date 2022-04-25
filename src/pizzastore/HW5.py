from collections import namedtuple
from collections import deque
import itertools
import random
Pizza = namedtuple("Pizza", ["ind", "name", "price", "description"])
pizzas = [
    Pizza(0, "Hawaii", 135, "Base + pineapple + chicken + cheese"),
    Pizza(1, "BBQ", 140, "Base + cheese + bacon + chicken + mushrooms"),
    Pizza(2, "Pepperoni", 150, "Base + mozzarella + pepperoni"),
    Pizza(3, "Margarita", 120, "Base + mozzarella + extracheese"),
    Pizza(4, "Texas", 155, "Base + onions + mushrooms + 4 types of meat"),
    Pizza(5, "Spicy", 130, "Base + pepperoni + bacon + tomatoes + jalapeno"),
    Pizza(6, "Munich", 210, "Base + ham + bavarian sausages + tomatoes"),
    Pizza(7, "Tuna", 190, "Base + mozzarella + tuna"),
    Pizza(8, "Provence", 215, "Base + ham + tomatoes + pepperoni"),
    Pizza(9, "Five cheeses", 230, "Base + cheddar + mozzarella + parmesan+ feta + bergader blue"),
    Pizza(10, "Vegan", 180, "Base + spinach + feta + tomatoes + olives")
]

def greetings():
    print("Welcome to the best pizzeria in Kyiv - ARSENAL!")
    print("To view the menu - enter 1")
    print("Exit - 0")
    print("To see pizzas that cost more than 150 -enter 2", "To see the queue - enter 3", sep="\n")


def print_menu(l):
    print("You can see our menu:")
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
            print_menu(pizzas)
        case "2":
            print_filter(pizzas, 150)
        case "3":
            deque_tables()
        case _:
            print("Wrong input")
            print("Please, try again!")