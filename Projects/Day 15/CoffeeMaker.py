import Data

WATER = Data.resources['water']
COFFEE = Data.resources['coffee']
MILK = Data.resources['milk']
MONEY = 0
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def check_coffee(answer):
    resources = []
    global WATER, MILK, COFFEE, MONEY
    if answer == 'espresso':
        WATER -= Data.MENU['espresso']['ingredients']['water']
        COFFEE -= Data.MENU['espresso']['ingredients']['coffee']
        for i in WATER, COFFEE:
            resources.append(i)
    elif answer == 'latte':
        WATER -= Data.MENU['latte']['ingredients']['water']
        MILK -= Data.MENU['latte']['ingredients']['milk']
        COFFEE -= Data.MENU['latte']['ingredients']['coffee']
        for i in WATER, COFFEE, MILK:
            resources.append(i)
    elif answer == 'cappuccino':
        WATER -= Data.MENU['cappuccino']['ingredients']['water']
        MILK -= Data.MENU['cappuccino']['ingredients']['milk']
        COFFEE -= Data.MENU['cappuccino']['ingredients']['coffee']
        for i in WATER, COFFEE, MILK:
            resources.append(i)
    return resources


def get_resources_of_answer(answer):
    data = []
    if answer != 'report':
        water = Data.MENU[answer]['ingredients']['water']
        coffee = Data.MENU[answer]['ingredients']['coffee']
        if answer != 'espresso':
            milk = Data.MENU[answer]['ingredients']['milk']
            for i in water, coffee, milk:
                data.append(i)
        else:
            for i in water, coffee:
                data.append(i)
        return data


def get_cost_of_coffee(answer):
    cost = Data.MENU[answer]['cost']
    return cost


def check_enough(resources, data, answer):
    global WATER, MILK, COFFEE
    if answer != 'report':
        if (resources[0] - data[0]) < 0:
            WATER += data[0]
            print("Sorry there is not enough water.")
            return False
        elif (resources[1] - data[1]) <= 0 and answer != 'espresso':
            MILK += data[1]
            print("Sorry there is not enough milk.")
            return False
        elif (resources[1] - data[1] <= 0) and answer == 'espresso':
            COFFEE += data[1]
            print("Sorry there is not enough coffee.")
            return False
        elif answer != 'espresso':
            if (resources[2] - data[2]) <= 0:
                COFFEE += data[2]
                print("Sorry there is not enough coffee.")
                return False
    return True


def paying_in_pennies(answer):
    global MONEY
    cost = get_cost_of_coffee(answer)
    print("Please insert coins.")
    quarters_amount = int(input("how many quarters?: "))
    dimes_amount = int(input("how many dimes?: "))
    nickles_amount = int(input("how many nickles?: "))
    pennies_amount = int(input("how many pennies?: "))
    total = (QUARTERS*quarters_amount) + (DIMES*dimes_amount) + (NICKLES*nickles_amount) + (PENNIES*pennies_amount)
    if total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {answer}. Enjoy!")
    elif total == cost:
        print("Here is your {answer}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
    MONEY += cost


WORKING = True
MONEY = 0
resource = []

while WORKING:
    ANSWER = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ANSWER == 'report':
        print(f"Water: {WATER}ml\nMilk: {MILK}g\nCoffee: {COFFEE}g\nMoney: ${round(MONEY, 2)}")
    elif ANSWER == 'off':
        WORKING = False
    else:
        data_of_answer = get_resources_of_answer(ANSWER)
        for i in WATER, COFFEE, MILK:
            resource.append(i)
        check_coffee(ANSWER)
    if ANSWER != 'report' and ANSWER != 'off':
        checker = check_enough(resource, data_of_answer, ANSWER)
        if checker:
            paying_in_pennies(ANSWER)
    resource = []




