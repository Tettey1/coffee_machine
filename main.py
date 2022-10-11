from menu import MENU, resources


def is_resource_sufficient(drink_order):
    """Returns True if order can be made and false if resources is insufficient"""
    for item in drink_order:
        if drink_order[item] > resources[item]:
            print(f'Sorry not enough {item}')
            return False
    return True


machine_money = 0


def process_coins():
    """Returns the total amount calculated from coins inserted"""
    total = 0
    total += int(input('How many quarters: ')) * 0.25
    total += int(input('How many dimes: ')) * 0.1
    total += int(input('How many nickles: ')) * 0.05
    total += int(input('How many pennies: ')) * 0.01
    return round(total, 2)


def make_coffee(drink_name, order):
    """Deduct the required resources needed to make coffee"""
    for item in order:
        resources[item] -= order[item]
    print(f'Here is your {drink_name}.Enjoy!')


def transaction_successful(drink_cost, money_entered):
    """Returns True if money is accepted and false if money is insufficient"""
    if money_entered >= drink_cost:
        global machine_money
        change = round(money_entered - drink_cost, 2)
        if change > 0:
            print(f'Here is ${change} in change')
        machine_money += round(money_entered, 2)
        return True
    else:
        print('Sorry Not enough money. Money refunded')
        return False


def print_report():
    """returns the current resources available to make coffee"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g')


off = False
money_paid = 0
while not off:
    coffee_order = input('What would you like? (espresso)/latte/cappuccino): ').lower()
    if coffee_order == 'off':
        off = True
    elif coffee_order == 'report':
        print_report()
        print(f'Money: ${machine_money}')
    else:
        order_items = MENU[coffee_order]
        if is_resource_sufficient(order_items["ingredients"]):
            print('Please insert coins')
            money_paid = process_coins()
            if transaction_successful(order_items["cost"], money_paid):
                make_coffee(coffee_order, order_items["ingredients"])
            else:
                machine_money -= money_paid
