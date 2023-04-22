
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BlockManager:
    def __init__(self):
        self.y_cos = [50, 100, 150]
        self.x_cos = [350, 250, 150, 50, -50, -150, -250, -350]
        self.all_blocks = []
        self.num_y = 0
        self.num_x = 0


    def make_blocks(self):
            if self.num_y <= 2:
                num = Turtle("square")
                num.speed(0)
                num.penup()
                num.shapesize(stretch_wid=2, stretch_len=5)
                num.color(random.choice(COLORS))
                num.setpos(self.x_cos[self.num_x], self.y_cos[self.num_y])
                self.all_blocks.append(num)
                self.num_x += 1
                if self.num_x > 7:
                    self.num_x = 0
                    self.num_y += 1


















