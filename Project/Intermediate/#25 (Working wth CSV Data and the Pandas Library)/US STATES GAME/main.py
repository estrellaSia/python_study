import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif" #실제 파일 이름과 똑같이 써야 함, 그렇지 않으면 _tkinter.TclError: couldn't open "blank_state_img.gif": no such file or directory 오류 날 수 있음
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?") # 문자열 입력을 위한 대화 상자 창을 띄움, 매개변수 title=> 대화 상자 창의 제목, prompt=> 주로 어떤 정보를 입력해야 하는지 설명하는 텍스트
print(answer_state)