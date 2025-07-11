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

def make_selection(choice):
    if choice == "off":
        print("Goodbye, shutting down for maintenance")
        machine_state = False

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(choice):
    """Check the resources needed to make the selected drink
    against the resources available"""
    for key in MENU[choice]["ingredients"]:
        if resources[key] < MENU[choice]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return
        else:
            return True

def accept_payment(choice):
    """Ask the user for payment and compute the total received, if amount
    is more than cost of drink, proceed to make drink"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    payment = ((quarters * 25) + (dimes * 10) + (nickles * 5) + pennies) / 100
    change = round((payment - MENU[choice]["cost"]), 2)
    if payment >= MENU[choice]["cost"]:
        print(f"Here is ${change } in change.")
        return payment
    else:
        print("Sorry that's not enough money. Money refunded.")
        return

def make_drink(choice):
    for key in MENU[choice]["ingredients"]:
        resources[key] -= MENU[choice]["ingredients"][key]
    print(f"Here is your {choice} ☕️. Enjoy!")



money = 0
machine_state = True
while machine_state:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    make_selection(user_choice)
    if user_choice == "off":
        # print("Goodbye, shutting down for maintenance")
        machine_state = False

    # TODO-1 Print report
    elif user_choice == "report":
        print_report()

    # TODO-2 Check if resources are sufficient
    else:
        if check_resources(user_choice):

            # TODO-3 Process coins
            # TODO-4 Check transaction successful
            accept_payment(user_choice)
            money += MENU[user_choice]["cost"]
            # TODO-5 Make Coffee and update resources
            make_drink(user_choice)
