import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.tolist()

while len(guessed_states) < 50:

    answer = turtle.textinput(title=f"{len(guessed_states)}/50. Guess the state", prompt="What's another state name?").title()

    if answer == "Exit":
        break

    if answer in guessed_states:
        pass

    elif answer in state_list:
        guessed_states.append(answer)
        guessed_state_data = state_data[state_data.state == answer]
        tim.goto(guessed_state_data.x.item(), guessed_state_data.y.item())
        tim.write(answer, move=False, align='left', font=('Arial', 12, 'normal'))

        if len(guessed_states) == 50:
            tim.goto(0,0)
            tim.write("Congrats you got all 50", move=False, align='left', font=('Arial', 24, 'normal'))

outstanding_states = []
for state in state_list:
    if state not in guessed_states:
        outstanding_states.append(state)

all_outstanding_states = pandas.DataFrame(outstanding_states)

all_outstanding_states.to_csv("states_to_learn.csv")

screen.exitonclick()
