# Turtle Challenge 5 - Draw a Spirograph

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100) #반지름: 100
        tim.setheading(tim.heading() + size_of_gap) #turtle.heading() : 현재 거북이가 바라보는 각도

draw_spirograph(5) #매번 5도씩 기울어지면서 그려짐