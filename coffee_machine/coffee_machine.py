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
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}
money = 0


def report(resources):
    water_quantity = int(resources["water"])
    milk_quantity = int(resources["milk"])
    coffee_quantity = int(resources["coffee"])
    print(f"Water: {water_quantity} ml")
    print(f"Milk: {milk_quantity} ml")
    print(f"coffee: {coffee_quantity} g")
    print(f"Money: {money} $")


def menu_item(item):

    money_inserted = calculate_money()
    if money_inserted >= MENU[item]["cost"]:
        print(f" Enjoy, Here is your {item}...")

        money_refund = money_inserted - MENU[item]["cost"]

        resources["water"] -= MENU[item]["ingredients"]["water"]
        resources["milk"] -= MENU[item]["ingredients"]["milk"]
        resources["coffee"] -= MENU[item]["ingredients"]["coffee"]

        if money_refund > 0:
            print(f" Here is your {round(money_refund,2)} $ in change...")
            return money + MENU[item]["cost"]

    else:
        print(f"Sorry Insufficient amount..Money refunded")


def check_resources():
    water_quantity = int(resources["water"])
    milk_quantity = int(resources["milk"])
    coffee_quantity = int(resources["coffee"])

    if water_quantity >= 200 and milk_quantity >= 150 and coffee_quantity >= 24 and decision == "latte":
        return True
    elif water_quantity >= 50 and coffee_quantity >= 18 and decision == "espresso":
        return True
    elif water_quantity >= 250 and milk_quantity >= 100 and coffee_quantity >= 24 and decision == "cappuccino":
        return True

def calculate_money():
    print(" Insert coins..")
    quarters = int(input("how many quarters?.."))
    dimes = int(input("how many dimes?.."))
    nickels = int(input("how many nickels?.."))
    pennies = int(input("how many pennies?.."))
    money_inserted = (quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01)
    return money_inserted

is_end=True
while is_end :
    decision = str(input("What would you like..(espresso/latte/cappuccino)...."))

    if decision == "report":
        report(resources)

    if decision == "off":
        is_end= False

    if decision == "espresso" or decision == "latte" or decision == "cappuccino":
        if check_resources():
          money += menu_item(decision)
        else:
            print("Insufficient_resources.. Money Refunded..")
            is_end = False
    else:
         print(" Sorry !.. Choose from the menu..")
         is_end= False

