# This is a coffee brewing project.
logo = """


                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'


"""


def report():
    global storage
    storage = {"water": 300, "milk": 200, "coffee": 100}
    water = storage["water"]
    milk = storage["milk"]
    coffee = storage["coffee"]

    return f"""
        Water:{water}
        Milk:{milk}
        Coffee:{coffee}
        """


report()


def calculate_money():
    global total_money
    penny = int(input("how many pennies? ->"))
    nickel = int(input("how many nickels? ->"))
    dime = int(input("how many dimes? ->"))
    quater = int(input("how many quaters? ->"))
    total = [penny * 0.01, nickel * 0.05, dime * 0.10, quater * 0.25]
    total_money = sum(total)
    return total_money


def make_latte():
    global latte
    latte = {"water": 200, "milk": 150, "coffee": 24, "price": 2.50}
    if latte["coffee"] > storage["coffee"]:
        print("Sorry there is not enough coffee.")
    elif latte["milk"] > storage["milk"]:
        print("Sorry there is not enough milk.")
    elif latte["water"] > storage["water"]:
        print("Sorry there is not enough water.")
    else:
        calculate_money()
        if latte["price"] < total_money:
            print(
                f"Your Coffee is on your way. Here is your {(round(total_money-latte['price'],2))} change."
            )
            storage["coffee"] -= latte["coffee"]
            storage["milk"] -= latte["milk"]
            storage["water"] -= latte["water"]

        elif latte["price"] > total_money:
            print("Sorry, that's not enough money. Money refunded")
        else:
            print("Thankyou for buying a Latte.Your Coffee is on your way.")
            storage["coffee"] -= latte["coffee"]
            storage["milk"] -= latte["milk"]
            storage["water"] -= latte["water"]


def make_espresso():
    global espresso
    global end_of_program
    espresso = {"water": 50, "milk": 0, "coffee": 18, "price": 1.50}
    if espresso["coffee"] > storage["coffee"]:
        print("Sorry there is not enough coffee.")
        end_of_program = True
    elif espresso["milk"] > storage["milk"]:
        print("Sorry there is not enough milk.")
    elif espresso["water"] > storage["water"]:
        print("Sorry there is not enough water.")
        end_of_program = True
    else:
        calculate_money()
        if espresso["price"] < total_money:
            print(
                f"Your Coffee is on your way. Here is your {(round(total_money-espresso['price'],2))} change."
            )
            storage["coffee"] -= espresso["coffee"]
            storage["milk"] -= espresso["milk"]
            storage["water"] -= espresso["water"]
        elif espresso["price"] > total_money:
            print("Sorry, that's not enough money. Money refunded")
        else:
            print("Thankyou for buying an Espresso.Your Coffee is on your way.")
            storage["coffee"] -= espresso["coffee"]
            storage["milk"] -= espresso["milk"]
            storage["water"] -= espresso["water"]


def make_cappuccino():
    global cappuccino
    cappuccino = {"water": 250, "milk": 100, "coffee": 24, "price": 3.00}
    if cappuccino["coffee"] > storage["coffee"]:
        print("Sorry there is not enough coffee.")
    elif cappuccino["milk"] > storage["milk"]:
        print("Sorry there is not enough milk.")
    elif cappuccino["water"] > storage["water"]:
        print("Sorry there is not enough water.")
    else:
        calculate_money()
        if cappuccino["price"] < total_money:
            print(
                f"Your Coffee is on your way. Here is your {(round(total_money-cappuccino['price'],2))} change."
            )
            storage["coffee"] -= cappuccino["coffee"]
            storage["milk"] -= cappuccino["milk"]
            storage["water"] -= cappuccino["water"]
        elif cappuccino["price"] > total_money:
            print("Sorry, that's not enough money. Money refunded")
        else:
            print("Thankyou for buying an cappuccino.Your Coffee is on your way.")
            storage["coffee"] -= cappuccino["coffee"]
            storage["milk"] -= cappuccino["milk"]
            storage["water"] -= cappuccino["water"]


end_of_program = False
while end_of_program == False:
    print(logo)
    order = input("What would you like? (espresso/latte/cappuccino):\n-->").lower()
    if order == "report":
        print(report())
    elif order == "espresso":
        make_espresso()
    elif order == "latte":
        make_latte()
    elif order == "cappuccino":
        make_cappuccino()
    else:
        print("Please enter a valid command")
print("Please re-fill the Machine with supplies.")
