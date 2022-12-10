from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"what will you like? {options}: ")
    if choice.lower() == "off":
        is_on = False
    elif choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_enough_money = money_machine.make_payment(drink.cost)
        if is_enough_money and is_enough_ingredients:
            coffee_maker.make_coffee(drink)
