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
}

total_coins = 0
def order():
    global total_coins
    for ing in MENU[guess]["ingredients"].keys():
        resources[ing] -= MENU[guess]["ingredients"][ing]
    total_coins += MENU[guess]["cost"]


def report():
    print(f" Water: {resources['water']}\n Milk: {resources['milk']} \n \
    Coffee: {resources['coffee']} \n Coins: {total_coins}")


def resourses_total():
    nullres = False
    for key in MENU[guess]["ingredients"]:
        if resources[key] < MENU[guess]["ingredients"][key]:
            print(f"Sorry, there is not enough {[key]}")
            nullres =  True
    return nullres

def payment():
    quarters = input("How many quarters?:")
    total_quarters = int(quarters) * 0.25
    dimes = input("How many dimes?:")
    total_dimes = int(dimes) * 0.10
    nickles = input("How many nickles?:")
    total_nickles = int(nickles) * 0.05
    pennies = input("How many pennies?:")
    total_pennies = int(pennies) * 0.01
    total = float(total_quarters + total_dimes + total_nickles + total_pennies)
    if total < MENU[guess]["cost"]:
        print("Sorry, that's not enough money. Money refunded")
    elif total == MENU[guess]["cost"]:
        print(f"Here is $0.0 in change. Here is your {guess}. Enjoy!")
        order()
    elif total > MENU[guess]["cost"]:
        change = round((total - MENU[guess]["cost"]),2)
        print(f"Here is ${change} in change.Here is your {guess}. Enjoy!")
        order()


continue_customer = True

while continue_customer:
    guess = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if guess == 'off':
        continue_customer = False
    elif guess == 'report':
        report()
    elif guess == 'espresso' or guess == 'latte' or guess == 'cappuccino':
        tot = MENU[guess]["cost"]
        if resourses_total()==True:
            continue_customer = False
            continue
        if resourses_total() == False:
         print(f"You need to pay {tot}. Insert coins.")
         payment()


