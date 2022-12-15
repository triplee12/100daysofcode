#!/usr/bin/python3
#!/bin/env/python3
"""Pizza order challenge"""
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size.upper() == "S":
    print("Price for small pizza is $15.")
    price = 15
    if add_pepperoni.upper() == "Y":
        price += 2
elif size.upper() == "M":
    print("Price for medium pizza is $20.")
    price = 20
    if add_pepperoni.upper() == "Y":
        price += 3
elif size.upper() == "L":
    print("Price for large pizza is $25.")
    price = 25
    if add_pepperoni.upper() == "Y":
        price += 3
else:
    print("Unknown command|:")
if extra_cheese.upper() == "Y":
    price += 1

print(f"Your total price is ${price}.")
