from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.color("white")
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score:02d}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def win(self, team):
        self.clear()
        self.write(f"{team} WINS!", align=ALIGNMENT, font=FONT)

    def play_again(self):
        self.clear()
