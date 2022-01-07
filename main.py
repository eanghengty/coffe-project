MENU = {
    "expresso":{
        "ingredient":{
            "water":50,
            "coffee":18
        },
        "cost":1.5
    },
    "latte":{
        "ingredient":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredient":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":3.0
    }

}

def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("please insert coin:")
    total=int(input("how many quarter?: ")) * 0.25
    total+=int(input("how many dimes?: ")) * 0.1
    total+=int(input("how many nickles?: ")) * 0.05
    total+= int(input("how many pennies?")) * 0.01
    return total



profit=0
resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":profit
}

def make_coffee(drink_name, order_ingredient):
        for item in order_ingredient:
            drink_name[item] -= order_ingredient[item]
        print(f"here is your {drink_name}. enjoy.")



def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"here is this ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that is not enough money")
        return False
is_on = True

while is_on:
    choice=input("what would you like? (expresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice=="report":
        print(f'water : {resources["water"]}')
        print(f'milk : {resources["milk"]}')
        print(f'coffee : {resources["coffee"]}')
        print(f'money: ${profit}')
    else:
        drink=MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredient"]):
            payment=process_coins()
            if(is_transaction_successful(payment,drink["cost"])):
                make_coffee(choice , drink["ingredient"])
