from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 20, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highest_score=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_score_board()
    def update_score_board(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highest_score}", False,ALIGNMENT ,FONT )
    def reset(self):
        if self.score>self.highest_score:

            with open("data.txt", mode="w") as new_score:
                new_score.write(str(self.score))
        self.score=0
        self.update_score_board()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)
    def eaten(self):
        self.score += 1

        self.update_score_board()





