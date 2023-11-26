import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_state_img.gif" #실제 파일 이름과 똑같이 써야 함, 그렇지 않으면 _tkinter.TclError: couldn't open "blank_state_img.gif": no such file or directory 오류 날 수 있음
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()