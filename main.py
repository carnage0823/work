from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


while is_on:
    options = menu.get_items()
    choice = input(f"what would you like {options} :")
    if choice == "off":
        is_on = False
    elif choice == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            machine.make_coffee(drink)
