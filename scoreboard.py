from turtle import Turtle
lives = 3

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        self.life = 3

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 230)
        self.write(f"Score: {self.score}", align="center", font=("courier", 28, "normal"))
        self.goto(200, 230)
        self.write(f"Lives: {lives}", align="center", font=("courier", 28, "normal"))
        if lives < 1:
            self.goto(0, -100)
            self.write("GAME OVER", align="center", font=("courier", 28, "normal"))


    def point(self):
        self.score += 1
        self.update_scoreboard()

    def check_life(self):
        global lives
        if self.life >= 1:
            self.life -= 1
            lives -= 1
            self.update_scoreboard()



