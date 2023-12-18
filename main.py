import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from title import Title
from again import Again

# Default parameters for game
WIDTH = 800
HEIGHT = 600
WIN_SCORE = 10

# Initialize screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.listen()


def play():
    # Draw dashed line
    dashed = Turtle()
    dashed.penup()
    dashed.color("white")
    dashed.setheading(270)
    dashed.backward(HEIGHT / 2)

    for i in range(int(HEIGHT / 2)):
        dashed.pendown()
        dashed.forward(10)
        dashed.penup()
        dashed.forward(10)

    # Draw Title screen
    title = Title(WIDTH, HEIGHT, WIN_SCORE)
    screen.onkeypress(title.game_start, "space")
    while title.waiting:
        screen.update()

    # Initialize Paddles
    r_paddle = Paddle((WIDTH / 2 - 50, 0))
    l_paddle = Paddle((WIDTH / 2 * -1 + 50, 0))

    # Take user inputs
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")

    # Initialize Scoreboards
    r_score = Scoreboard((WIDTH / 2 / 2, HEIGHT / 2 * 0.8))
    l_score = Scoreboard((WIDTH / 2 / 2 * -1, HEIGHT / 2 * 0.8))

    # Initialize ball
    ball = Ball()

    # Play the game
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with wall
        if ball.ycor() >= HEIGHT / 2 + - 10 or ball.ycor() <= HEIGHT / 2 * -1 + 10:
            ball.bounce()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() >= WIDTH / 2 - 60 \
                or ball.distance(l_paddle) < 50 and ball.xcor() <= WIDTH / 2 * -1 + 60:
            ball.hit()

        # Detect when right paddle misses
        if ball.xcor() >= WIDTH / 2 - 10:
            ball.miss()
            l_score.increase_score()

        # Detect when left paddle misses
        if ball.xcor() <= WIDTH / 2 * -1 + 10:
            ball.miss()
            r_score.increase_score()

        # End the game
        if r_score.score == WIN_SCORE:
            r_score.win("RIGHT")
            game_is_on = False
            time.sleep(1)
            Again()
        elif l_score.score == WIN_SCORE:
            l_score.win("LEFT")
            game_is_on = False
            time.sleep(1)
            Again()

    # Start a new game or close
    if not game_is_on:
        screen.onkey(play_again, "y")
        screen.onkey(exit_game, "n")


def play_again():
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    play()


def exit_game():
    exit()


# Plays the game
play()

screen.mainloop()
