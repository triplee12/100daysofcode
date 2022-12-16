#!/usr/bin/python3
#!/bin/env/python3
"""Treasure map"""
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
t_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
row = position[0]
col = position[1]

indx = t_map[int(row) - 1]
indx[int(col) - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
