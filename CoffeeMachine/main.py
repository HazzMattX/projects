MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1. Print a report of all coffe machine resources
# TODO: 2. Check if resources are sufficient to make offer.
# TODO: 3. Turn machine by entering 'off' in the prompt.
# TODO: 4.  Check for enough money.
# TODO: 5. Ask what customer would they like?
# TODO: 6. Successful payment?
# TODO 7. Make coffee.

def pay():
    print("Please pay with money.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
def print_report():
    """Prints a report of all coffee machine resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True
def is_transaction_successful(money_received, drink_cost):
    change = round(money_received - drink_cost, 2)
    print(f"Your change is ${change}.")
    if money_received > drink_cost:
        global money
        money += drink_cost
        return True
    else:
        print("Error. Not enough money.")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}. ☕️")
is_on = True
while is_on:
    choice = input("What would you like? 'espresso', 'latte', or cappucino. \nYou can also type ' report' or 'off'. ")
    if choice == "report":
        print(print_report())
    elif choice == "off":
        print("Goodbye!")
        is_on = False
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = pay()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])