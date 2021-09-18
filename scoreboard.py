from turtle import Turtle

ALIGNMENT = "center"
FONT = ("ubuntu", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
         with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)
        

    def game_start(self):
        self.write(f"5 seconds to start", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    
        
        self.write(f"GAME OVER | Final Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
