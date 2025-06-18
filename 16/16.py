from menu16 import Menu
from coffee_maker16 import CoffeeMaker
from money_machine16 import MoneyMachine
menu_of_rest = Menu()
coffee_machine = CoffeeMaker()
money_in_machine = MoneyMachine()
turn_off = False
while not turn_off:
    user_req = input(f"What would you like? {menu_of_rest.get_items()}: ")
    if user_req == "off":
        turn_off = True
    elif user_req == "report":
        coffee_machine.report()
        money_in_machine.report()
    else:
        item = menu_of_rest.find_drink(user_req)
        if item != None:
            if item.name == "latte":
                index = 0
            elif item.name == "espresso":
                index = 1
            else:
                index = 2
            sufficient_resources = coffee_machine.is_resource_sufficient(menu_of_rest.menu[index])
            if sufficient_resources:
                cost_of_item = menu_of_rest.menu[index].cost
                enough_money = money_in_machine.make_payment(cost_of_item)
                if enough_money:
                    coffee_machine.make_coffee(menu_of_rest.menu[index])

#WELL WELL WELL, THERE IS MORE SIMPLER WAY OF DOING THIS! BUT I GUESS MY BARAIN JUST DONT WORK THAT WAY. I NEED TO GO AROUND AND FIGURE WHAT ACTUALLY WORKS. ALSO SINCE IT WORKS I AM NOT MODIFING IT FURTHER, AND NOTEE THAT IN THE EASY CODE - ELSE BLOCK HAS LIKE 5 STMTS.