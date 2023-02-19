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


# TODO: 6. Then update the report after giving the required coffee to the consumer:
def update_resources(water_used, milk_used, coffee_used, earned_money):
    water_remain = resources['water'] - water_used
    milk_remain = resources['milk'] - milk_used
    coffee_remain = resources['coffee'] - coffee_used

    resources['water'] = water_remain
    resources['milk'] = milk_remain
    resources['coffee'] = coffee_remain
    resources['money'] = earned_money


def is_drink_available(drink):
    if MENU[drink]['ingredients']['water'] > resources['water']:
        print("water not available")
        # resources_available = False
        return False
    if 'milk' in MENU[drink]['ingredients'].keys() and MENU[drink]['ingredients']['milk'] > resources['milk']:
        print('milk not available')
        # resources_available = False
        return False
    if MENU[drink]['ingredients']['coffee'] > resources['coffee']:
        print('coffee not available')
        # resources_available = False
        return False
    return True


def ingredients_required(user_drink):
    if 'milk' in MENU[user_drink]['ingredients'].keys():
        milk_need = MENU[user_drink]['ingredients']['milk']
        # return MENU[user_drink]['ingredients']['milk']
    else:
        milk_need = 0
    if 'water' in MENU[user_drink]['ingredients'].keys():
        water_need = MENU[user_drink]['ingredients']['water']
        # return MENU[user_drink]['ingredients']['water']
    else:
        water_need = 0
    if 'coffee' in MENU[user_drink]['ingredients'].keys():
        coffee_need = MENU[user_drink]['ingredients']['coffee']
        # return MENU[user_drink]['ingredients']['coffee']
    else:
        coffee_need = 0

    return water_need, milk_need, coffee_need


# TODO: 1. make a report on available resources present  in the coffee-machine:
def coffe_machine_report():
    resources.setdefault("money", 0)
    report = resources

    return report


def coffee_machine():
    money_earned = 0
    resources_available = True
    while resources_available:
        # TODO: 2. Aks the user to choose variety of coffee.
        user_drink = input("What would you like? (espresso/latte/cappuccino):")

        if user_drink in MENU.keys():
            # TODO: 4. Check if required chosen coffee's resources is available in the coffee machine:
            drink_available = is_drink_available(user_drink)
            if drink_available:
                # TODO: 3. Ask the user the available coins he have.
                quarter_money = int(input('how many quarters?'))  # 0.25
                dimes_money = int(input('how many dimes?:'))  # 0.10
                nickles_money = int(input('how many nickles?:'))  # 0.05
                pennies_money = int(input('how many pennies?:'))  # 0.01

                total_user_money_have = quarter_money * 0.25 + dimes_money * 0.10 + nickles_money * 0.05 + pennies_money * 0.01
                cost_of_drink = MENU[user_drink]['cost']
                # TODO: 5. After checking if total cost of the coffee is sufficient for chose coffee:
                if total_user_money_have < cost_of_drink:
                    print(f"Sorry!🤔🤔 it's not enough money to buy the drink {user_drink}")
                    continue

                change_money = round(total_user_money_have - cost_of_drink, 2)
                money_earned += cost_of_drink
                # print('$', total_user_money_have)
                # print('Money earned: ', money_earned)
                print(f'Here is ${change_money} in change.')
                print(f"here is your {user_drink}☕")

                water_used, milk_used, coffee_used = ingredients_required(user_drink)

                update_resources(water_used, milk_used, coffee_used, money_earned)
            else:
                print(f"Oh! sorry 😊😊resources for {user_drink} not available")
                continue

        elif user_drink == "report":
            present_available_resources = coffe_machine_report()
            for item, quantity in present_available_resources.items():
                if item == 'water' or item == 'milk':
                    print(item, ': ', quantity, 'ml')
                if item == 'coffee':
                    print(item, ': ', quantity, 'g')
                if item == 'money':
                    print(item, ': ', '$', quantity)
        elif user_drink == 'exit':
            print('Thank you,🙏🙏 for having the drink')
            break
        else:
            print("Invalid Input! 👿👿")

coffee_machine()
