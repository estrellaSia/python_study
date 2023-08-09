# Create a Snake Class & Move to OOP

from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #background color
screen.title("My Snake Game")
screen.tracer(0) #터틀 애니메이션 on/off, update를 하지 않는 이상 화면은 갱신되지 x기 때문에 어떤 동작을 수행하는지 볼 수 x

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # 각 세그먼트가 이동하고 나서 0.1s 지연시간이 걸림

    snake.move()

screen.exitonclick()