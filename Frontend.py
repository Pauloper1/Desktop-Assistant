from tkinter import *
from tkinter.ttk import*
from tkinter import scrolledtext
from turtle import width
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from aiAssistant import *


#---------Styling----------
WindowColor = '#90ee90'
TitleColor = '#2364AA'
ConvoColor = '#f9cff2'


window = Tk()
window.configure(bg=WindowColor)
q1 = queries()
window.geometry('500x550')
window.title('Voice Assistant')
window.iconbitmap('r', './Images/Assistant.ico')
window.resizable(False, False)

#---------Menu----------


#---------Title----------
Title = Label(window, text='DESKTOP VOICE ASSISTANT',font=("Times New Roman", 15, 'bold'))
Title.pack(pady=10)
#---------Functions----------


    # Define Our Images
on = (Image.open("./Images/On.png"))
off = (Image.open("./Images/off.png"))
on = on.resize((60, 30), Image.ANTIALIAS)
on = ImageTk.PhotoImage(on)
off = off.resize((60, 30), Image.ANTIALIAS)
off = ImageTk.PhotoImage(off)


def ConvoButton():
    q1.Convo()
    print(q1.r.pause_threshold)
    q1.r.pause_threshold = 1
    Convo.insert(10.0, f'User : {q1.query}\nEren : {q1.res}\n')
    q1.speak(q1.res)


#---------Button----------
btnImage = PhotoImage(file='./Images/btn4.png')
btn = Button(window, image=btnImage, width=100, command=ConvoButton)
btn.pack(pady=5)


#---------Textarea----------
Convo = scrolledtext.ScrolledText(
    window, width=40, height=10, font=("Times New Roman", 15), bg=ConvoColor)

Convo.pack()

mainloop()
