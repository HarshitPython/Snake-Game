from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background.gif")
screen.title("Snake Game")
screen.tracer(0)
screen.register_shape("apple.gif")
screen.register_shape("snake.gif")
# screen.register_shape("try_again.gif")
screen.register_shape("snake_head.gif")
screen.register_shape("snake_head_right.gif")
screen.register_shape("snake_head_up.gif")
screen.register_shape("snake_head_down.gif")

snake = Snake()

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
    

screen.exitonclick()
