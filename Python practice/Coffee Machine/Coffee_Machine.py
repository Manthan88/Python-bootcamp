from coffee_data import *

def check_resource(choices):
    for item in choices:
        if choices.get(item,0) > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def calculate():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction(money_received,cost):
    change = round((money_received - cost),2)
    if money_received < cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif money_received > cost:
        resources['money'] += cost
        print(f"Here is ${change} in change")
        return True
    else:
        resources['money'] += cost
        return True
    
    
def adjust_resources(choices):
    for item in choices:
        resources[item] -= choices.get(item,0)

is_on = True

while is_on:
    choice = input("What would you like? Espresso/Latte/Cappuccino: ").lower()
    if choice not in commands:
        print("This command is not available, Try again")
    elif choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']} ml"),
        print(f"Milk: {resources['milk']} ml"),
        print(f"Coffee: {resources['coffee']} g"),
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[choice]
        if check_resource(drink['ingredients']):
            payment = calculate()
            if transaction(payment, drink['cost']):
                adjust_resources(drink['ingredients'])
                print(f'Here is your {choice}. Enjoy!')