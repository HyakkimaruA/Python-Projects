from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

correct = True

# Keeps looping until user tells to stop
while correct:

    # Gets all the drinks that the machine offers.
    items = menu.get_items()

    # Gets the input (drink) of the user.
    drink = input(f"What do you want to drink? ({items}): ").lower()

    # Given a valid drink.
    if drink in items:
        drink_obj = menu.find_drink(drink)
        sufficient_money = money_machine.make_payment(drink_obj.cost)

        name = drink_obj.name
        cost = drink_obj.cost
        ingredients = drink_obj.ingredients

        # If sufficient amount of money given by the user.
        if sufficient_money:

            # Checks whether there are resources left within the machine.
            corrected = coffee_maker.is_resource_sufficient(drink_obj)
            if corrected:
                coffee_maker.make_coffee(drink_obj)

    # Report the resources, if user asks for them.
    elif drink == 'report':
        coffee_maker.report()
        money_machine.report()

    # Go out the 'while-loop' if user wants to turn it off.
    elif drink == 'off':
        correct = False

    # Given a drink, which the machine doesn't offer.
    else:
        print("Sorry, unfortunately I don't offer this.....")
        print(f"I only offer these drinks: {items}.\n")
