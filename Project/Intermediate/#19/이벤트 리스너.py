from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
#space 키보드 누르면 --> move_forwards 실행됨
# 함수를 다른 함수로 안에 넣을 시 안에 ()쓰지 x
screen.exitonclick()