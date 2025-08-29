MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0
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
    "milk": 1000,
    "coffee": 100,
}
total_sum=0
money=0

from asci import logo
print (logo)

#TODO : 2. check resources sufficient
##check against the recipe and then give user feedback
def check_resource(item1):
    """check resources by using two functions less_item then no coffee and enough then insert coins"""
    item = (MENU[item1]["ingredients"])
    item2= (MENU[item1]["cost"])
    def less_item():
        """look for less item and give feedback that it is less"""
        defi_item={"water":item["water"] < resources["water"], "coffee": item["coffee"] < resources["coffee"],
                   "milk" : item["milk"] < resources["milk"]}
        for _ in defi_item:
            if not defi_item[_]:
                return _
        return None
    if item["water"] < resources["water"] and item["coffee"]< resources["coffee"] and item["milk"]<resources["milk"]:
        def coin_insert():
            """process coins and also multiply and add to find the sum"""
            coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
            print("Please insert coins:")
            quarter= float(input("How many quarters?: "))
            dime= float(input("How many dimes?: "))
            nickle=float(input("How many nickels?: "))
            pennie= float(input("How many pennies?: "))
            global total_sum
            total_sum=((coins["quarters"]*quarter) + (coins["dimes"] * dime)
                       + (coins["nickles"] * nickle) + (coins["pennies"] * pennie))
            def transaction(x,y):
                if x>y:
                    print("Sorry not enough money. Your money is refunded")
                if x<=y:
                    print(f"This is your {item1} \u2615. Enjoy")
                    change=y-x
                    f_change=round(change,2)
                    print("Here is your", f_change,"dollars")
                    global money
                    money+=x
            transaction(item2,total_sum)
            global resources
            resources={"water":resources["water"]-item["water"],"milk":resources["milk"]-item["milk"],"coffee":
                       resources["coffee"]-item["coffee"]}
        coin_insert()

    else:
        print("Sorry there is not enough", less_item())
# TODO: 1.print report and input for coffee
def coffee_choice():
    """coffee selection and report generation"""
    ask_user=True
    while ask_user:
        reports = (f"Water : {resources["water"]}ml \nMilk : {resources["milk"]}ml "
                   f"\nCoffee : {resources["coffee"]}g \nMoney : ${money}")
        choose=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choose == "report":
            print(reports)
        elif choose == "off":
            return
        elif choose == "espresso" or "latte" or "cappuccino":
            check_resource(choose)
coffee_choice()
