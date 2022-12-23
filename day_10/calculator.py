#!/usr/bin/python3

logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

(Regular Calculator)
           _            _       _
          | |          | |     | |
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
'''

# Add function
def add(n1, n2):
    """Return summation of two numbers."""
    return n1 + n2

# Subtraction function
def subtract(n1, n2):
    """Return subtraction result of two numbers."""
    return n1 - n2

# Multiplication function
def multiply(n1, n2):
    """Return product of two numbers."""
    return n1 * n2

# Division function
def divide(n1, n2):
    """Return division result of two numbers."""
    try:
        answer = n1 / n2
        return answer
    except ZeroDivisionError:
        print("Can not divide by zero.")

math_dict = {
        "+": add, "-": subtract, "*": multiply, "/": divide,
}

def calculator():
    """Calculate and return the result of user's integer input."""
    print(logo)
    print("Welcome to the Pycalculator")
    first_num = float(input("What's the first number?: "))

    for key in math_dict:
        print(key)
    continue_ = "y"

    while continue_ == "y":
        operator = input("Pick an operator: ")
        second_num = float(input("What's the next number?: "))
        calculate = math_dict[operator]
        result = calculate(first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {result}")
        continue_ = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_ == "y":
            first_num = result
        else:
            continue_ = "n"
            calculator()

calculator()
