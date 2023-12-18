from turtle import Turtle

class Again(Turtle):
    def __init__(self):
        super().__init__()
        self.go_again = True
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.write("Play again? Press 'Y' or 'N'", align='center', font=('Courier', 18, 'bold'))
