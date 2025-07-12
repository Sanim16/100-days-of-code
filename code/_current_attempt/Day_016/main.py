from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee = CoffeeMaker()
my_profit = MoneyMachine()


is_on = True
while is_on:
    drink_choice = input(f"What would you like? {my_menu.get_items()}:")
    if drink_choice == "off":
        print("Going into maintenance mode, Goodbye")
        is_on = False
    elif drink_choice == "report":
        my_coffee.report()
        my_profit.report()
    else:
        selection = my_menu.find_drink(drink_choice)
        if selection is not None:
            if my_coffee.is_resource_sufficient(selection):
                if my_profit.make_payment(selection.cost):
                    my_coffee.make_coffee(selection)
