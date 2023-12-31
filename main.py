from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) #Turn off Auto Update


# Creating a snake object using Snake class
snake = Snake() 
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.left,key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    # Collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()




    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            
           



screen.exitonclick()