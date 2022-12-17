#!/usr/bin/python3
#!/bin/env/python3
"""Calculate the sum of all the even numbers from 1 to 100"""
total_even = 0
for num in range(1, 101):
    if num % 2 == 0:
        total_even += num

print(total_even)
