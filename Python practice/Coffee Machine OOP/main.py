from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeeMaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()} ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffeeMaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)