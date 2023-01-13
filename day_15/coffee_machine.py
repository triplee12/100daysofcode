#!/usr/bin/python3
"""coffee_machine module"""


resources = {
        "Water":   100000,
        "Milk":    50000,
        "Coffee":  10000,
        "Balance": 0.0,
}

drinks = {
        "espresso":   4.25,
        "latte":      5.01,
        "cappuccino": 6.25,
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


turn = "on"
while turn == "on":
    request_ = prompt(drinks)
    if request_ == "off":
        turn = "off"
    
    report(resources)
