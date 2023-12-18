from turtle import Turtle
import time

FONT = ('Courier', 14, 'normal')


class Title(Turtle):
    def __init__(self, width, height, win_score):
        super().__init__()
        self.waiting = True
        self.win_score = win_score
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.write(f"PONG", align='center', font=('Courier', 48, 'bold'))
        self.goto(0, -50)
        self.write(f"Press space to start", align='center', font=('Courier', 24, 'normal'))

        # Left controls
        self.goto(-(width / 2) + 50, -(height / 2) + 90)
        self.write(f"Left", align='left', font=FONT)
        self.goto(-(width / 2) + 50, -(height / 2) + 60)
        self.write(f"Up: W", align='left', font=FONT)
        self.goto(-(width / 2) + 50, -(height / 2) + 30)
        self.write(f"Down: S", align='left', font=FONT)

        # Right controls
        self.goto((width / 2) - 50, -(height / 2) + 90)
        self.write(f"Right", align='right', font=FONT)
        self.goto((width / 2) - 50, -(height / 2) + 60)
        self.write(f"Up: ↑", align='right', font=FONT)
        self.goto((width / 2) - 50, -(height / 2) + 30)
        self.write(f"Down: ↓", align='right', font=FONT)

    def game_start(self):
        if self.waiting:
            self.clear()
            self.goto(0, 0)
            self.write("3", align='center', font=('Courier', 24, 'bold'))
            time.sleep(1)
            self.clear()
            self.write("2", align='center', font=('Courier', 24, 'bold'))
            time.sleep(1)
            self.clear()
            self.write("1", align='center', font=('Courier', 24, 'bold'))
            time.sleep(1)
            self.clear()
            self.write(f"First to {self.win_score} wins!", align='center', font=('Courier', 24, 'normal'))
            time.sleep(1)
            self.clear()
            self.waiting = False
