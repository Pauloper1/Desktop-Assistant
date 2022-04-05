from tkinter import *
from tkinter import scrolledtext
from turtle import width

window = Tk()
window.geometry('500x550')
window.title('Voice Assistant')
#---------Button----------
btnImage = PhotoImage(file='btn4.png')
btn = Button(window, image=btnImage, width=100, height=100, borderwidth=0)
btn.pack()

#---------Textarea----------
Convo = scrolledtext.ScrolledText(window, width=40, height=10)
Convo.insert(10.0, 'Hello , this is Desktop Voice Assistant')
Convo.configure(state='disabled')
Convo.pack()
#---------Menu----------

mainloop()
