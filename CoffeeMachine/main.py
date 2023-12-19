MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0
}


def print_resource(item):
    if item == "coffee":
        print(f"Coffee: {resources[item]}g")
    elif item == "Money":
        print(f"{item}: ${resources[item]}")
    else:
        print(f"{item.capitalize()}: {resources[item]}ml")


def check_resources(drink):
    if drink == "report":
        for item in resources:
            print_resource(item)
        return 0
    else:
        for ingri in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][ingri] > resources[ingri] and ingri != "Money":
                print(f"Sorry there is not enough {ingri}.")
                return 0
        return 1


def check_money(drink):
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    sum= 0.25 * quarters + 0.10*dimes+0.05*nickles+0.01*pennies
    if sum < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif sum > MENU[drink]["cost"]:
        print(f"Here is ${round(sum-MENU[drink]["cost"], 2)} in change.")
        return 1


def update_resources(drink):
    for ingri in MENU[drink]["ingredients"]:
        resources[ingri] -= MENU[drink]["ingredients"][ingri]
    resources["Money"] += MENU[drink]["cost"]
    return 1


off = False
while not off:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        off = True
        continue
    if check_resources(drink) == 0:  # will print what is missing , print report
        continue
    if check_money(drink) == 0: # ask for coins, calc the sum of them and check if there is enough and print the change:Here is $16.9 in change.
        continue
    update_resources(drink) # update resources after an order
    print(f"Here is your {drink} ☕️. Enjoy!")




