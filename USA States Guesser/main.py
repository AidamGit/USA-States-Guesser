import turtle
import pandas

display = turtle.Screen()
display.setup(height=491, width=725)
display.bgpic("blank_states_img.gif")

state_name_display = turtle.Turtle()
state_name_display.penup()
state_name_display.hideturtle()

data = pandas.read_csv("50_states.csv")
state_names = data["state"].tolist()

states_guessed = 0
while states_guessed < 50:

    guess = display.textinput(title=f"{states_guessed}/50 States Guessed", prompt="Guess a state").title()
    if guess in state_names:
        states_guessed += 1

        # sets coordinates for state_name_display to write the state name on
        state_name_display.setx(int(data[data["state"] == guess]["x"]))
        state_name_display.sety(int(data[data["state"] == guess]["y"]))
        state_name_display.pendown()
        state_name_display.write(arg=guess, font=("arial", 7, "bold"), align="center")
        state_name_display.penup()

        state_names.remove(guess)

    if guess == "Exit" or guess == "Finish" or guess == "End":
        pandas.DataFrame(state_names).to_csv("States to Learn.csv")
        break

# after the game ends, the states that haven't been guessed will be labeled by red
for state in state_names:

    state_name_display.setx(int(data[data["state"] == state]["x"]))
    state_name_display.sety(int(data[data["state"] == state]["y"]))
    state_name_display.pendown()
    state_name_display.pencolor("red")
    state_name_display.write(arg=state, font=("arial", 7, "bold"), align="center")
    state_name_display.penup()

turtle.done()
