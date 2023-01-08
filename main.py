MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml \nMilk: {milk}ml\nCoffee: {coffee}g\nMoney ${money}")


def start():
    print("What would you like? espresso/latte/cappuccino")
    coffee_type = input()
    return coffee_type


def resource(n):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    needed_water = MENU[n]["ingredients"]["water"]
    needed_milk = MENU[n]["ingredients"]["milk"]
    needed_coffee = MENU[n]["ingredients"]["coffee"]
    if water < needed_water:
        print("Sorry there is not enough water")
        return False
    elif milk < needed_milk:
        print("Sorry there is not enough milk")
        return False
    elif coffee < needed_coffee:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def cash():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes "))
    nickles = int(input("How many nickles "))
    pennies = int(input("How many pennies "))
    dollars = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return dollars


def brew(i):
    needed_water = MENU[i]["ingredients"]["water"]
    needed_milk = MENU[i]["ingredients"]["milk"]
    needed_coffee = MENU[i]["ingredients"]["coffee"]
    resources["water"] -= needed_water
    resources["milk"] -= needed_milk
    resources["coffee"] -= needed_coffee
    print(f"Here is your {i}. Enjoy!")


def make_coffee():
    coffee_type = start()
    if coffee_type == "off":
        print("Turning off")
        return
    elif coffee_type == "report":
        report()
        make_coffee()
    enough = resource(coffee_type)
    if enough == False:
        make_coffee()
    elif enough == True:
        money = cash()
        money_needed = MENU[coffee_type]["cost"]
        if money < money_needed:
            print("Sorry thats not enough money. Money refunded")
            make_coffee()
        elif money > money_needed:
            change = round(money - money_needed, 2)
            print(f"your change is ${change}")
            resources["money"] += money_needed
            brew(coffee_type)
            make_coffee()


make_coffee()
