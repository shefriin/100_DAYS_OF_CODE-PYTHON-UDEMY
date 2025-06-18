money_in_machine = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def coffee_machine():
    global money_in_machine
    global resources
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


    def print_report():
        for key in resources:
            if key == "milk" or key == "water":
                print(f"{key}: {resources[key]}ml")
            else:
                print(f"{key}: {resources[key]}g")
        global money_in_machine
        print(f"Money: ${money_in_machine}")

    def check_resources(thing):
        if resources["water"] - MENU[thing]["ingredients"]["water"] < 0:
            return "water"
        elif resources["coffee"] - MENU[thing]["ingredients"]["coffee"] < 0:
            return "coffee"
        if thing != "espresso":
            if resources["milk"] - MENU[thing]["ingredients"]["milk"] < 0:
                return "milk"
        return True

    def make_thing(thing):
        if thing != "espresso":
            for key in resources:
                resources[key] -= MENU[thing]["ingredients"][key]
        else:
            resources["water"] -= MENU[thing]["ingredients"]["water"]
            resources["coffee"] -= MENU[thing]["ingredients"]["coffee"]
        # print("WELL WELL,,,", resources)

    user_req = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_req == "report":
        print_report()
        return True
    elif user_req == "off":
        return False
    elif user_req == "espresso" or user_req == "latte" or user_req == "cappuccino":
        resources_left = check_resources(user_req)
    else:
        print("INVALID BUTTON ENTERED.")
        return True

    if resources_left != True:
        print(f"Sorry there is not enough {resources_left}.")
        return True

    print("Please insert coins:")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickels = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    money_on_user = quarters + dimes + nickels + pennies

    if money_on_user < MENU[user_req]["cost"]:
        print("Sorry that's not enough money. Money refunded!")
        return True

    money_in_machine += MENU[user_req]["cost"]

    if money_on_user > MENU[user_req]["cost"]:
        change = round((money_on_user-MENU[user_req]["cost"]),2)
        # print(f"change: {change},,,,, money_mach: {money_in_machine},,,,, user_mach:{MENU[user_req]["cost"]}")
        print(f"Here is ${change} in change.")

    make_thing(user_req)
    print(f"Here is your {user_req} ☕. Enjoy!")
    return True

machine_on = True
while machine_on:
    machine_on = coffee_machine()