# Turtle Challenge 4-2 - Generate a Random Walk(Generate Random RGB Colours)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)  #turtle.color(R,G,B) 형식으로 색을 선택할 때 입력 방식을 바꿈

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))