from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu= Menu()
make_coffee= CoffeeMaker()
payment=MoneyMachine()
while 1:
    drink = input(f"What would you like? (espresso/latte/cappuccino/): ")
    if drink == "off":
        break
    elif item := menu.find_drink(drink):
        if make_coffee.is_resource_sufficient(item) and payment.make_payment(item.cost):
            make_coffee.make_coffee(item)
    elif drink=="report":
        make_coffee.report()
        payment.report()