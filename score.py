from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Century", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(x=0,y=260)
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.updatescore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.updatescore()

    # def game_over(self):
    #     self.clear()
    #     self.color("blue")
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", align="center", font=FONT)
    #     self.goto(0, -40)
    #     self.write(f"You're final score is: {self.score}", align="center", font=FONT)

