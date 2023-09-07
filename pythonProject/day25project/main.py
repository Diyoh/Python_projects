import turtle

import pandas
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) <= 50:
    score = f"{len(guessed_state)} / 50"
    user_state = screen.textinput(title=f" {score} Guessed", prompt="Whats another states name?")
    answer_state = user_state.title()
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        print(new_data)
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        all_states.remove(answer_state)
    if answer_state == "Exit":
        exit

# states_to_learn = pd.DataFrame(all_states)
# states_to_learn.to_csv("missing_states")
# screen.exitonclick()
# turtle.mainloop()

# screen.exitonclick()
