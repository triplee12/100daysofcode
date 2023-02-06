"""Work timer graphical user interface program"""
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_counter():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(can_text, text=f"00 : 00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_counter():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
        counter(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)
        counter(short_break_sec)
    else:
        timer_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
        counter(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def counter(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(can_text, text=f"{count_min} : {count_sec}")
    if count > 0:
       timer = window.after(1000, counter, count - 1)
    else:
        start_counter()
        mark_good = ""
        sessions = math.floor(reps / 2)
        for _ in range(sessions):
            mark_good += "✔"
            checkmark_label.config(text=mark_good, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=226, height=226, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="clock")
canvas.create_image(113, 113, image=photo)
can_text = canvas.create_text(113, 115, text="00 : 00", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", font=(FONT_NAME, 20, "bold"), highlightthickness=0, bg=YELLOW, command=start_counter)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", font=(FONT_NAME, 20, "bold"), highlightthickness=0, bg=YELLOW, command=reset_counter)
reset_btn.grid(column=3, row=3)

checkmark_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=4)


window.mainloop()
