from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) #화면의 폭을 500으로, 높이를 400으로 설정
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") #팝업창을 띄워 사용자가 메시지와 제목을 읽고 텍스트를 입력하도록 함
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # 거북이 모양으로 설정
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
        #터틀 객체=> 40x40크기, 250지점에 도달할 때를 탐지한다면 터틀은 이미 결승선을 지나있을 것임
        #따라서 230지점에 도달했을 때를 탐지해야함(250-(40/2)=230)
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle. forward(rand_distance)

screen.exitonclick()