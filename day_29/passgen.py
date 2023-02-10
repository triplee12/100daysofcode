#!/usr/bin/env python3
"""Password generator gui"""
from tkinter import *

window = Tk()
window.title("Password Generator")
window.config(padx=10, pady=10, bg="#fff")
canvas = Canvas(width=200, height=200, bg="#fff", highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website = Label(text="Website:", fg="#000", bg="#fff", font=("Arial", 12, "normal"))
website.grid(column=0, row=1)
webentry = Entry(width=35)
webentry.grid(column=1, row=1, columnspan=2)
email_or_username = Label(text="Email/Username:", fg="#000", bg="#fff", font=("Arial", 12, "normal"))
email_or_username.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
password = Label(text="Password:", fg="#000", bg="#fff", font=("Arial", 12, "normal"))
password.grid(column=0, row=3)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)
pass_btn = Button(text="Generate Password", fg="#000", bg="#fff", highlightthickness=0)
pass_btn.grid(column=2, row=3)
add = Button(text="Add", width=36, fg="#000", bg="green", highlightthickness=0)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
