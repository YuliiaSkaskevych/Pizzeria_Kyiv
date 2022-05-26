from items.exception import MyException
from items.receipt import Receipt
from items.receiptline import ReceiptLine
from items.pizzastore import PizzaStore
import random

pizzastore = PizzaStore()

while True:
    pizzastore.greetings()
    menu=input("Please, enter the number: ")
    match menu:
        case "0":
            print("Good luck!")
            break
        case "1":
            pizzastore.print_menu(pizzastore.pizzas)
        case "2":
            while True:
                try:
                    a = int(input("Enter the price more than you want: "))
                    if a <= 0:
                        raise MyException("Wrong input!")
                    filter = [element for element in pizzastore.pizzas if element.price > a]
                    pizzastore.print_menu(filter)
                    break
                except MyException:
                    print("Error! Number must be > 0")
                except ValueError:
                    print("Error! You must enter the number!")
        case "3":
            check = Receipt(pizzastore.get_table())
            a = random.sample(pizzastore.pizzas, random.randint(1, 5))
            for pizzas_items in a:
                check.add_line(ReceiptLine(pizzas_items, random.randint(1, 5)))
            pizzastore.add_receipt(check)
            pizzastore.print_receipts()
        case "4":
            pizzastore.deque_tables()
        case "5":
            while True:
                try:
                    print("If you want exit - enter 0")
                    c = int(input("Please enter the number of receipt you want to change: "))
                    if c == 0:
                        break
                    check = pizzastore.receipts[c-1]
                    print(check)
                    p = input("What pizza do you want to change: ")
                    for line in check.lines:
                        if p == line.pizza.name:
                            pizzastore.editor()
                            change = int(input("You choice: "))
                            if change == 1:
                                h= int(input("Enter the number: "))
                                line.change_number_pizzas(h)
                                print(check)
                                break
                            if change == 2:
                                m = int(input("Enter the amount: "))
                                line.amount_pizzas(m)
                                print(check)
                                break
                            if change == 3 and len(check.lines)>1:
                                check.lines.remove(line)
                                print(check)
                                break
                    else:
                        print("Error input!")
                except ValueError:
                    print("Error input!")
        case _:
            print("Wrong input")
            print("Please, try again!")