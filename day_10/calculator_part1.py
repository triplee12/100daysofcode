#!/usr/bin/python3

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
    return n1 / n2

math_dict = {
        "+": add, "-": subtract, "*": multiply, "/": divide,
}
first_num = int(input("What's the first number?: "))

for key in math_dict:
    print(key)
operator = input("Pick an operator: ")
second_num = int(input("What's the next number?: "))
calculate = math_dict[operator]
result = calculate(first_num, second_num)
print(f"{first_num} {operator} {second_num} = {result}")

#continue_ = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
