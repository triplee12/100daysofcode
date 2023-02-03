#!/usr/bin/env python3
"""50 states of USA game"""
import turtle as tl
import pandas as pd
import time

DATA_PATH = "50_states.csv"
STATE_IMG = "blank_states_img.gif"

screen = tl.Screen()
screen.addshape(STATE_IMG)
tl.shape(STATE_IMG)
screen.title("U.S. States Guess Game")

# Read the 50 states of U.S
data = pd.read_csv(DATA_PATH)
guessed_state = []

while len(guessed_state) < 50:
    try:
        guess = screen.textinput(f"{len(guessed_state)}/50 Guess the states of USA", prompt= "What's another state's name?").title()
        all_states = data.state.to_list()
        state_data = data[data.state == guess]
        state_name = state_data.state
        state_xcor = int(state_data.x)
        state_ycor = int(state_data.y)

        if guess == "Exit":
            # Convert the states not guessed by the user to csv
            not_guess = []
            for state in all_states:
                if state not in guessed_state:
                    not_guess.append(state)
            df = pd.DataFrame(not_guess)
            df.to_csv("not_guess_states.csv")
            break

        # Check if guess in all_states
        if guess in all_states:
            guessed_state.append(guess)
            # Place state_name on the map using state_xcor and state_ycor
            tostate = tl.Turtle()
            tostate.penup()
            tostate.ht()
            tostate.goto(state_xcor, state_ycor)
            tostate.write(guess, font=('Arial', 8, 'normal'))
    except TypeError:
        break

