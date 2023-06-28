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

should_continue = True
deducted_resources = {}  # Initialize deducted_resources outside the loop
total_money = 0  # Initialize total_money outside the loop

def payment(ans):
    cost = MENU[ans]["cost"]
    print(f"The total cost is ${cost:.2f}. Please insert your coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_money = quarters + dimes + nickels + pennies

    if total_money == cost:
        print(f"Enjoy your {ans}!")
        return cost
    elif total_money > cost:
        change = total_money - cost
        print(f"Here is your change: ${change:.2f}. Enjoy your {ans}!")
        return cost
    else:
        print("Sorry, your money is not sufficient. Refunding your money.")
        return 0

def check_resources(ans):
    required_ingredients = MENU[ans]["ingredients"]
    insufficient_ingredients = []

    for ingredient, required_quantity in required_ingredients.items():
        if ingredient in resources and required_quantity <= resources[ingredient]:
            continue
        else:
            insufficient_ingredients.append(ingredient)

    if len(insufficient_ingredients) == 0:
        deducted_resources = {}  # To store the deducted resources
        for ingredient, required_quantity in required_ingredients.items():
            resources[ingredient] -= required_quantity
            deducted_resources[ingredient] = required_quantity

        return payment(ans), deducted_resources
    else:
        print("Sorry, the following ingredients are not available in sufficient quantity:")
        for ingredient in insufficient_ingredients:
            print(f"- {ingredient}")
        return 0, {}

def report(total_money, deducted_resources):
    print(f"Total money: ${total_money:.2f}")
    print("Remaining Resources:")
    for ingredient, quantity in resources.items():
        print(f"{ingredient}: {quantity}")
    if deducted_resources:
        print("Deducted Resources:")
        for ingredient, quantity in deducted_resources.items():
            print(f"{ingredient}: {quantity}")
    else:
        print("No deducted resources yet.")

while should_continue:
    ans = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

    if ans in MENU:
        sumt, deducted_resources = check_resources(ans)
        if sumt != 0:
            total_money += sumt
    elif ans == "report":
        report(total_money, deducted_resources)
    elif ans=="off":
      print("Devise is turned off")
      should_continue=False
    else:
        print("Invalid input.")
