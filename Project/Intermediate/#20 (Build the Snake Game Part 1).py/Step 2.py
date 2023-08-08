# Animating the Snake Segments on Screen

from turtle import Screen, Turtle
import time

tim = Turtle()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #background color
screen.title("My Snake Game")
screen.tracer(0) #터틀 애니메이션 on/off, update를 하지 않는 이상 화면은 갱신되지 x기 때문에 어떤 동작을 수행하는지 볼 수 x

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # 각 세그먼트가 이동하고 나서 0.1s 지연시간이 걸림

    for seg_num in range(len(segments) - 1, 0,-1): #start:범위의 시작점, stop:범위가 끝나는 지점, step: 증가폭
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
