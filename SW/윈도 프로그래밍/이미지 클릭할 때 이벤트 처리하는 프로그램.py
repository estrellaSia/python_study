# 마우스 버튼(3개)을 클릭하면 대화상자가 출력되는 이벤트 처리

from tkinter import*
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "C:/Users/minky/Desktop/내장 메모리/GIF/rabbit.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()