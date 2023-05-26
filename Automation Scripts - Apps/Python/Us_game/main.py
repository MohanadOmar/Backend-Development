from turtle import Screen, Turtle
import pandas
import time

screen = Screen()
display = Turtle()
display.penup()
display.hideturtle()
screen.bgpic("blank_states_img.gif")

# Data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# Brain Quiz
guessed_correct = []
states_to_learn = []

while len(guessed_correct) < 50:
    time.sleep(0.2)
    user_guess = screen.textinput(title=f"{len(guessed_correct)}/50 States Correct", prompt="What's Another State Name:").title()

    if user_guess == "Exit":
        for state in all_states:
            if state not in guessed_correct:
                states_to_learn.append(state)
        data = pandas.DataFrame(states_to_learn)
        data.to_csv("states_to_learn")
        break

    if user_guess in all_states and user_guess not in guessed_correct:
        state_data = data[data["state"] == user_guess]
        display.goto(x=int(state_data.x), y=int(state_data.y))
        display.write(arg=user_guess, font=("arial", 8, "bold"))
        guessed_correct.append(user_guess)
