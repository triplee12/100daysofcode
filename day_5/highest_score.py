#!/usr/bin/python3
#!/bin/env/python3
"""Highest score; get the maximum score from a list"""
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

maximum = 0

for score in student_scores:
    if score > maximum:
        maximum = score
print(f"The highest score in the class is {maximum}")
