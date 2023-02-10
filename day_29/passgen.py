#!/usr/bin/env python3
"""Password generator gui"""
from tkinter import *
from tkinter import messagebox

def save():
    """Saves user password to a file"""
    get_web = webentry.get()
    get_email = email_entry.get()
    get_pass = pass_entry.get()
    value = f"website:  {get_web}, email/username: {get_email}, password: {get_pass}"
    if get_web == "" or get_email == "" or get_pass == "":
        messagebox.showerror(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        msbox = messagebox.askokcancel(title="Do you want to save?", message=value)
        if msbox:
            webentry.delete(0, END)
            email_entry.delete(0, END)
            pass_entry.delete(0, END)
            with open("my_pass.txt", mode="a", encoding="utf-8") as pas:
                pas.write(f"{value}\n")

# Window settings
window = Tk()
window.title("Password Generator")
window.config(padx=10, pady=10, bg="#fff")
canvas = Canvas(width=200, height=200, bg="#fff", highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Label, entry for website
website = Label(text="Website:", fg="#000", bg="#fff", font=("Arial", 12, "normal"))
website.grid(column=0, row=1)
webentry = Entry(width=35)
webentry.grid(column=1, row=1, columnspan=2)
webentry.focus()

# Label, entry for email or username
email_or_username = Label(text="Email/Username:", fg="#000", bg="#fff", font=("Arial", 12, "normal"))
email_or_username.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

# Label, entry for password
password = Label(text="Password:", fg="#000", bg="#fff", font=("Arial", 12, "normal"))
password.grid(column=0, row=3)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)
pass_btn = Button(text="Generate Password", fg="#000", bg="#fff", highlightthickness=0)
pass_btn.grid(column=2, row=3)

# Button for add password
add = Button(text="Add", width=36, fg="#000", bg="green", highlightthickness=0, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
