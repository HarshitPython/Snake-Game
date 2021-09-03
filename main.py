from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background.gif")
screen.title("Snake Game")
screen.tracer(0)
screen.register_shape("apple.gif")
screen.register_shape("snake.gif")
screen.register_shape("snake_head.gif")
screen.register_shape("snake_head_right.gif")
screen.register_shape("snake_head_up.gif")
screen.register_shape("snake_head_down.gif")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()
        

    #Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
   
screen.exitonclick()
