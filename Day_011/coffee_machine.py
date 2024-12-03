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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def display_report(available_resources):
    """
    A function to display the available resources and money collected
    :param available_resources:
    :return:
    """
    for key in available_resources:
        print(f"{key}: {available_resources[key]}")

def check_resources(selection):
    """
    A function to check if available resources can make the selected drink
    :param selection:
    :return: True if resources can make selected drink and false if not
    """
    for key in MENU[selection]["ingredients"]:
        if resources[key] < MENU[selection]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False
        else:
            return True

def update_resources(selection):
    """
    A function to update the resources after successfully making the drink
    :param selection:
    :return:
    """
    for key in MENU[selection]["ingredients"]:
        resources[key] -= MENU[selection]["ingredients"][key]

def make_payment(selection):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    payment = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
    if payment >= MENU[selection]["cost"]:
        change = round((payment - MENU[selection]["cost"]), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {selection} ☕️.Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

money = 0
coffee_machine = True

while coffee_machine:
    report = {
        "Water": f"{resources['water']}ml",
        "Milk": f"{resources['milk']}ml",
        "Coffee": f"{resources['coffee']}g",
        "Money": f"${money}"
    }
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        exit()
    elif choice == "report":
        display_report(report)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            print("Please insert coins.")
            if make_payment(choice):
                money += MENU[choice]["cost"]
                update_resources(choice)
