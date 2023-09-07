from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.lives = 5
        with open("high_score.txt", mode="r") as S:
            contents = S.read()
        self.high_score = contents
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" Lives: {self.lives}  Score: {self.Score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reduce_lives(self):
        if self.lives > 0:
            self.lives -= 1
            self.update_scoreboard()

    def reset_score(self):
        if self.Score > int(self.high_score):
            self.high_score = self.Score
            with open("high_score.txt", mode="w") as U:
                U.write(f"{self.high_score}")
        self.Score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.write("GAME OVER", align="center",font=FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.Score += 1
        self.update_scoreboard()
