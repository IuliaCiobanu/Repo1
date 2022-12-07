from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def pad_position(self, x_pos, y_pos):
        self.penup()
        self.setpos(x_pos, y_pos)

    def move_up(self):
        y = self.ycor()
        self.sety(y + 40)

    def move_down(self):
        y = self.ycor()
        self.sety(y - 40)
