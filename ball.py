from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.add_x = 10
        self.add_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.add_x
        new_y = self.ycor() + self.add_y
        self.setpos(new_x, new_y)

    def bounce(self):
        self.add_y *= -1
        self.move()

    def hit(self):
        self.move_speed *= 0.9
        self.add_x *= -1
        self.move()

    def miss(self):
        self.move_speed = 0.1
        self.setpos(0, 0)
        self.hit()
