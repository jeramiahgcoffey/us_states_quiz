import turtle
import pandas
from state_generator import State
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
screen.setup(width=724, height=600)
screen.bgcolor("gray")


data = pandas.read_csv("50_states.csv")

list_of_states = list(data.state)


def return_coordinates(state):
    state_data = data[data.state == f"{state}"]
    x_coor = int(state_data.x)
    y_coor = int(state_data.y)
    state_coordinates = (x_coor, y_coor)
    return state_coordinates


correct_answers = 0
title = "Guess a State"

while correct_answers < 50:
    screen.update()

    if correct_answers > 0:
        title = f"{correct_answers}/50 States Guessed"

    answer_state = screen.textinput(title=title, prompt="What's the name of a state?\n"
                                                        "'Cancel' Ends Game.").title()
    if answer_state in list_of_states:
        correct_answers += 1
        return_coordinates(answer_state)
        state = State()
        state.show_state(name=answer_state, coor=return_coordinates(answer_state))
        time.sleep(0.75)





## This code helps extract state coordinates ##
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

screen.exitonclick()