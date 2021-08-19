from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("calibre", 16, "normal"))

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("calibre", 16, "bold"))
