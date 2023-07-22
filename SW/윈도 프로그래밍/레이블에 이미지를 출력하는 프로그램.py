from tkinter import *
window = Tk()

photo = PhotoImage(file = "C:/Users/minky/Desktop/내장 메모리/GIF/dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop