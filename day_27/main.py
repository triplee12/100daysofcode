#!/usr/bin/env python3
"""Miles to kilometer converter"""
from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("Miles To KM Converter")
window.config(padx=10, pady=10)

def converter():
    km = 1.6 * float(convert.get())
    result["text"] = round(km, 2)

convert = Entry(width=15)
convert.grid(column=1, row=0)

desc = Label(text="is equal to", font=("Arial", 20, "normal"))
desc.grid(column=0, row=1)
desc.config(padx=8, pady=5)

result = Label(text="0", font=("Arial", 24, "normal"))
result.grid(column=1, row=1)
result.config(padx=5, pady=5)

mile_l = Label(text="Miles", font=("Arial", 18, "normal"))
mile_l.grid(column=2, row=0)
mile_l.config(padx=10, pady=10)

btn = Button(text="Convert", command=converter)
btn.grid(column=1, row=2)
btn.config(padx=10, pady=10)

kilometer = Label(text="km", font=("Arial", 18, "normal"))
kilometer.grid(column=3, row=1)
kilometer.config(padx=5, pady=5)


window.mainloop()
