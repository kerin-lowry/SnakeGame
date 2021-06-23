from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    
    def __init__(self):
        self.snake_segments = []
        self.create()
        self.head = self.snake_segments[0]    
    
    
    def create(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)
    
    
    def reset_snake(self):
        for segment in self.snake_segments:
            segment.goto(3000, 3000)
        self.snake_segments.clear()
        self.create()
        self.head = self.snake_segments[0]
    
    
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
    
    
    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment-1].xcor()
            new_y = self.snake_segments[segment-1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)   


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)   


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)                               