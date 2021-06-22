from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ("Courier", 14, "normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.refresh()
        
        
    def refresh(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT_STYLE)
        
    
    def update(self):
        self.score += 1
        self.refresh() 
        
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font= FONT_STYLE)        