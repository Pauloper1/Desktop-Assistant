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


#---------SettingPage----------
def settingWindowFun():

    currentPauseValue = tk.DoubleVar()
    currentRateValue = tk.DoubleVar()

    settingWindow = tk.Tk()
    settingWindow.geometry('400x300')

    # ---------labels----------

    pause_lbl = tk.Label(settingWindow, text='Pause threshold ')
    pause_lbl.pack()

    Rate_lbl = tk.Label(settingWindow, text='Speech Rate')
    Rate_lbl.pack()

    pause_Val = tk.Label(settingWindow)
    pause_Val.pack()

    Rate_Val = tk.Label(settingWindow)
    Rate_Val.pack()
    # ---------Slider----------

    def get_Rate_value():
        return '{: .0f}'.format(currentRateValue.get())

    def get_pause_value():
        return '{: .1f}'.format(currentPauseValue.get())

    def PauseSlideChanged(currentPauseValue):
        pause_Val.configure(text=get_pause_value())

    def RateSlideChanged(currentRateValue):
        print(currentRateValue)
        Rate_Val.configure(text=get_Rate_value())

    Pause_slider = ttk.Scale(settingWindow, from_=0, to=1,
                             orient='horizontal', command=PauseSlideChanged, value=0.8)
    Pause_slider.pack()

    Rate_slider = ttk.Scale(settingWindow, from_=0, to=500,
                            orient='horizontal', command=RateSlideChanged, variable=currentRateValue, value=400)
    Rate_slider.pack()

    def setCommand():
        print(currentRateValue.get())
        q1.engine.setProperty('rate', currentRateValue)
        print(q1.engine.getProperty('rate'))

    setBtn = tk.Button(settingWindow, text='Set', command=setCommand)
    setBtn.pack()

    Ambient = Label(settingWindow, text='AmbientMode ')
    Ambient.pack()

    def switch():
        global is_on

        # Determine is on or off
        if is_on:
            on_button.config(image=off)
            is_on = False
        else:
            on_button.config(image=on)
            is_on = True

    # Define Our Images
    on = (Image.open("./Images/On.png"))
    off = (Image.open("./Images/off.png"))

    on = on.resize((60, 30), Image.ANTIALIAS)
    on = ImageTk.PhotoImage(on)

    off = off.resize((60, 30), Image.ANTIALIAS)
    off = ImageTk.PhotoImage(off)
    # Create A Button
    on_button = Button(settingWindow, image=on,  command=switch)
    on_button.pack(pady=50)


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
# Convo.insert(10.0, 'Hello , this is Desktop Voice Assistant')
# Convo.configure(state='disabled')
Convo.pack()


btnSetting = Button(window, text='Setting', command=settingWindowFun, width=20)
btnSetting.pack(pady=10)


mainloop()
