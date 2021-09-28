from menu import MENU, resources

resources["money"] = 0
machine = True
report = resources

while machine:

    order = input("what would you like to order (cappuccino , latte , espresso): ")

    if order == "off":
        machine = False

    def orders():
        if order == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
            return

        print("please insert the coins")
        quarters = int(input("how many quarters: "))
        quarters = quarters / 4
        dimes = int(input("how many dimes: "))
        dimes = dimes / 10
        nickels = int(input("how many nickels: "))
        nickels = nickels / 20
        penny = int(input("how many penny: "))
        penny = penny / 100
        payment = quarters + dimes + nickels + penny

        if order == "cappuccino":
            if MENU["cappuccino"]["ingredients"]["water"] < resources["water"] \
                    and MENU["cappuccino"]["ingredients"]["coffee"] < resources["coffee"]\
                    and MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]:

                if payment < MENU["cappuccino"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    return

                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

                change = payment - MENU["cappuccino"]["cost"]
                add_money = payment - change
                resources["money"] += add_money
                print(f"here is your change {change}")
                print("here is your cappuccino, enjoy!")
            else:
                if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
                    print("sorry not enough water")
                elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
                    print("sorry not enough coffee")
                elif MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]:
                    print("sorry not enough milf")
                return
        elif order == "latte":
            if MENU["latte"]["ingredients"]["water"] < resources["water"] \
                    and MENU["latte"]["ingredients"]["coffee"] < resources["coffee"]\
                    and MENU["latte"]["ingredients"]["milk"] < resources["milk"]:

                if payment < MENU["latte"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    return

                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]

                change = payment - MENU["latte"]["cost"]
                add_money = payment - change
                resources["money"] += add_money
                print(f"here is your change {change}")
                print("here is your order latte, enjoy!")
            else:
                if MENU["latte"]["ingredients"]["water"] > resources["water"]:
                    print("sorry not enough water")
                elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
                    print("sorry not enough coffee")
                elif MENU["latte"]["ingredients"]["milk"] < resources["milk"]:
                    print("sorry not enough milf")
                return
        elif order == "espresso":
            if MENU["espresso"]["ingredients"]["water"] < resources["water"] \
                    and MENU["espresso"]["ingredients"]["coffee"] < resources["coffee"]:

                if payment < MENU["espresso"]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    return

                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

                change = payment - MENU["espresso"]["cost"]
                add_money = payment - change
                resources["money"] += add_money
                print(f"here is your change {change}")
                print("here is your espresso, enjoy!")
            else:
                if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
                    print("sorry not enough water")
                elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
                    print("sorry not enough coffee")
                return
    if machine:
        orders()
