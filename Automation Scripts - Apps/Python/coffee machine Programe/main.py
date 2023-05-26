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


#########-----Code-----########

# Functions

# Report
def report(resources):
    for element in resources:
        print(f"{element}: {resources[element]}")


# Check Resources
def check_resources(resources, drink):
    #Resources sum
    sum_resources = 0
    for element in resources:
        sum_resources += resources[element]

    #Drink resources
    drink_resources = 0
    element = MENU[drink]["ingredients"]
    for i in MENU[drink]["ingredients"]:
        drink_resources += element[i]

    if sum_resources >= drink_resources:
        return True
    else:
        print("Not enough resources")


# Check Price
def check_price(price):
    total_money_inserted = 0

    print(f"\nThe price is: {price}$")

    inserted_quarters = int(input("How many quarters: "))
    quarter = inserted_quarters / 4

    inserted_dimes = int(input("How many dimes:"))
    dimes = inserted_dimes / 10

    inserted_nickles = int(input("How many nickles: "))
    nickles = inserted_nickles / 20

    inserted_pennies = int(input("How many pennies:"))
    pennies = inserted_pennies / 100

    total_money_inserted += quarter
    total_money_inserted += dimes
    total_money_inserted += nickles
    total_money_inserted += pennies

    change = round(total_money_inserted - price)

    if total_money_inserted == price:
        return True
    elif total_money_inserted > price:
        print(f"Here it is your change {change}$\n")
        return True
    else:
        print("Not enough money")
        return False


#Coffee Making
def coffee_making(drink, resources):
    element = MENU[drink]["ingredients"]
    for value in element:
        resources[value] -= element[value]
    print(f"Here it is your {drink}☕")





#Programe
def programe():
    drink = input("\nEspresso /Latte /Cappuccino /Report: ").lower()
    if drink == "report":
        report(resources)
    else:
        #Checking Price
        price = MENU[drink]["cost"]

        if check_resources(resources, drink) == True and check_price(price) == True:
            # Making our Coffee
            coffee_making(drink, resources)


turn_programe_off = False
while turn_programe_off == False:
    programe()