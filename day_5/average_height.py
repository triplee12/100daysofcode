#!/usr/bin/python3
#!/bin/env/python3
"""Average height"""
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_heights = 0
height_length = 0

for height in student_heights:
    total_heights += height # get the summation of student heights
    height_length += 1 # get the length of the list

average_height = total_heights / height_length # calculate the average
print(round(average_height))
