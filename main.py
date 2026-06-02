
from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Saina the Snake game.")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.eaten()


    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        score.reset()
        snake.reset()


    for segmen in snake.segment:
        if segmen == snake.head:
            pass
        elif snake.head.distance(segmen) <10:
            score.reset()
            snake.reset()






screen.exitonclick()