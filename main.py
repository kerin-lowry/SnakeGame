from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

#set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game - Kerin Lowry")
screen.tracer(0)

#create snake object, food object
snake = Snake()
food = Food()
score = Score()

# wait for keypress by user
screen.listen() 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down") 
screen.onkey(snake.left, "Left") 
screen.onkey(snake.right, "Right")    


#game loop
game_on = True
while game_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()
        
    #Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset_game()
        snake.reset_snake()
        #game_on = False
        #score.game_over()
        
        
    #detect collison with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset_snake()
            #game_on = False
            #score.game_over()


screen.exitonclick()