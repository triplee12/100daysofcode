#!/usr/bin/python3
#!/bin/env/python3
"""Python variable"""
a = input("a: ")
b = input("b: ")
print("Original value of a = {:d}".format(int(a)))
print("Original value of b = {:d}".format(int(b)))
a, b = b, a
print("Value of a and b after swift is\na = {:d}\nb = {:d}".format(int(a), int(b)))
