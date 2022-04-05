from tkinter import *
from tkinter import scrolledtext
from turtle import width

window = Tk()
window.geometry('500x550')

#---------Button----------
btnImage = PhotoImage(file='./Images/btn4.png')
btn = Button(window, image=btnImage, width=100, height=100, borderwidth=0)
btn.grid(column=10, row=0)

#---------Textarea----------
Convo = scrolledtext.ScrolledText(window, width=40, height=10)
Convo.insert(10.0, 'Hello')
Convo.configure(state='disabled')
Convo.grid(column=11, row=1)

#---------Menu----------

mainloop()
