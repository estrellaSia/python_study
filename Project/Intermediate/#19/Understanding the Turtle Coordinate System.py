#터틀 좌표계 이해하기

from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400) #화면의 폭을 500으로, 높이를 400으로 설정
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") #팝업창을 띄워 사용자가 메시지와 제목을 읽고 텍스트를 입력하도록 함
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")  # 거북이 모양으로 설정
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])


screen.exitonclick()