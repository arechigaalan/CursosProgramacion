from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if order == 'off':
        break
    elif order == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if drink:
            if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffe_maker.make_coffee(drink)
