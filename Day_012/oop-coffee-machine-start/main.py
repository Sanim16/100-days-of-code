from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem
coffee = CoffeeMaker()
money = MoneyMachine()

coffee_machine = True
while coffee_machine:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "report":
        coffee.report()
        money.report()
    elif choice == "off":
        exit()
    elif menu.find_drink(choice):
        if coffee.is_resource_sufficient(menu.find_drink(choice)):
            if money.make_payment(menu.find_drink(choice).cost):
                coffee.make_coffee(menu.find_drink(choice))
