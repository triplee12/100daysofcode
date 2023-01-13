#!/usr/bin/python3
"""coffee_machine module"""


# Available resources in the coffee machine
resources = {
        "Water":   100000,
        "Milk":    50000,
        "Coffee":  10000,
        "Balance": 0.0,
}

# Names of drinks and their prices
drinks = {
        "espresso":   4.25,
        "latte":      5.01,
        "cappuccino": 6.25,
}

# Recipe detail for coffee
recipes = {
        "espresso": {
            "water": 150,
            "milk":  50,
            "coffee": 70,
        },
        "latte": {
            "water": 200,
            "milk": 70,
            "coffee": 90,
        },
        "cappuccino": {
            "water": 200,
            "milk": 60,
            "coffee": 100,
        },
}


def prompt(drinks):
    """Prompts customer to enter his/her request and returns the
    request

    Args:
        drinks (dict): dictionary of drinks available in machine

    """
    request_ = input("What would you like? (espresso/latte/cappuccino): ").lower()

    for drink in drinks:
        if request_ == drink:
            return request_
        elif request_ == "off":
            return "off"


def report(obj):
    """Prints the current resources and it's available
    values

    Args:
        obj (dict): the resources object

    """
    for resource in obj:
        if resource == "Balance":
            print(f"{resource}: ${obj[resource]}")
            break
        print(f"{resource}: {obj[resource]}")


def check_resources(drinks, resources, request_, recipes):
    """Checks the availability of resources for the customer's
    request and returns True if enough resources

    Args:
        drinks (dict): drinks available in machine
        resources (dict): available resources
        request_ (str): user's request
        recipes (dict): ingredients of requested drink

    """
    if request_ in drinks:
        for drink in recipes.keys():
            if request_ == drink:
                for recipe, quantity in recipes[drink].items():
                    if recipe == "water" and resources["Water"] > quantity:
                        resources["Water"] -= quantity
                    elif recipe == "milk" and resources["Milk"] > quantity:
                        resources["Milk"] -= quantity
                    elif recipe == "coffee" and resources["Coffee"] > quantity:
                        resources["Coffee"] -= quantity
                    else:
                        print(f"Sorry there is not enough {recipe}.")
                break


turn = "on"
while turn == "on":
    request_ = prompt(drinks)
    check_resources(drinks, resources, request_, recipes)

    if request_ == "off":
        turn = "off" # Turn off the coffee machine
    report(resources)
