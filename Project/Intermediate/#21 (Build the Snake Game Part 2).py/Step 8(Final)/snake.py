from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #background color
screen.title("My Snake Game")
screen.tracer(0) #터틀 애니메이션 on/off, update를 하지 않는 이상 화면은 갱신되지 x기 때문에 어떤 동작을 수행하는지 볼 수 x

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect collision with food
    if snake.head.distance(food) < 15: #뱀의 머리부터 먹이까지의 거리
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or  snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        # 반복문을 통해 세그먼트를 가져오면 이 segments 리스트를 잘라주면 됨

screen.exitonclick()