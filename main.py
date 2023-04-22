from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from blocks import BlockManager

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

score = ScoreBoard()
paddle = Paddle((0, - 250))
ball = Ball()
blocks = BlockManager()


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
for num in range(24):
    blocks.make_blocks()
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.ycor() > 200:
        ball.bounce_y()
    if ball.distance(paddle) < 50 and ball.ycor() < -210:
        ball.bounce_ball_y()
    for block in blocks.all_blocks:
        for cor in blocks.x_cos:
            if ball.distance(block) < 50 and ball.xcor() < cor:
                block.goto(900, 700)
                ball.bounce_block()
                score.point()

    if ball.ycor() < -280:
        if score.life >= 1:
            ball.reset()
        score.check_life()

    if score.life == 0:
        game_is_on = False



screen.exitonclick()
