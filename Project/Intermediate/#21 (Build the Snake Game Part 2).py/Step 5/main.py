#Detect Collisions with Food

from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #background color
screen.title("My Snake Game")
screen.tracer(0) #터틀 애니메이션 on/off, update를 하지 않는 이상 화면은 갱신되지 x기 때문에 어떤 동작을 수행하는지 볼 수 x

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up") #위쪽 방향키가 눌리면 Up 함수가 불릴 것임
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # 화면 갱신
    time.sleep(0.1)  # 각 세그먼트가 이동하고 나서 0.1s 지연시간이 걸림(갱신 지연시키는 타이머를 써서 화면 갱신 횟수 조정)
    snake.move()

    #먹이 충돌 감지
    if snake.head.distance(food) < 15: #뱀의 머리부터 먹이까지의 거리
        food.refresh()


screen.exitonclick()
