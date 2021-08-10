from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_state(self, name, coor):
        self.goto(coor)
        self.write(f"{name}", align="center", font=("Arial", 12, "normal"))
