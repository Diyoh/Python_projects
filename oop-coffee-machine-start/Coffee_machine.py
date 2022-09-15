import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_machine = CoffeeMaker()
money = MoneyMachine()
# my_menu = MenuItem()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = (input(f"what will you like {options}  "))
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_machine.report()
        money.report()

    else:
        drink = menu.find_drink(choice)
        if my_coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                my_coffee_machine.make_coffee(drink)

