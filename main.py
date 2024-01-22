from turtle import Turtle, Screen
import pandas
turtle = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.title("U.S. states game")
screen.addshape(image)
turtle.shape(image)
screen.setup(800,600)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

matched_states = []

while len(matched_states) < 50:
    answer = screen.textinput(f"{len(matched_states)}/{50}", "What is another state's name ?").title()

    if answer == "Exit":
        missing_states = []
        # for state in all_states:
        #     if state not in matched_states:
        #         missing_states.append(state)
        state_list = [missing_states.append(state) for state in all_states if state not in matched_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")

        break
    if answer in all_states:
       matched_states.append(answer)
       t = Turtle()
       t.hideturtle()
       t.penup()
       state_data = data[data.state == answer]
       t.goto(int(state_data.x), int(state_data.y))
       t.write(answer)


