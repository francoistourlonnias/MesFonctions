"""
tk-destroy.py
"""
from Tkinter import *

def makeWindow():
    win = Tk()
    lab1 = Label(win, text='New Window').pack(side=TOP)
    butn1 = Button(win, text='Press to exit',
    command=win.destroy)
    butn1.pack(side=BOTTOM)

win1 = Tk()
b1 = Button(win1, text='Window Maker',command=makeWindow)
b1.pack(side=BOTTOM)
mainloop()
