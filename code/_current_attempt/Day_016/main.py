from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MyMenu = Menu()
MyCoffee = CoffeeMaker()
MyProfit = MoneyMachine()


is_on = True
while is_on:
    drink_choice = input(f"What would you like? {MyMenu.get_items()}:")
    if drink_choice == "off":
        print("Going into maintenance mode, Goodbye")
        is_on = False
    elif drink_choice == "report":
        MyCoffee.report()
        MyProfit.report()
    else:
        selection = MyMenu.find_drink(drink_choice)
        if selection is not None:
            if MyCoffee.is_resource_sufficient(selection):
                if MyProfit.make_payment(selection.cost):
                    MyCoffee.make_coffee(selection)

