from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
# TODO: 1. Print a report of all coffe machine resources
# TODO: 2. Check if resources are sufficient to make offer.
# TODO: 3. Turn machine by entering 'off' in the prompt.
# TODO: 4.  Check for enough money.
# TODO: 5. Ask what customer would they like?
# TODO: 6. Successful payment?
# TODO 7. Make coffee.

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}. \nYou can also type ' report' or 'off'. ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("Goodbye!")
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
