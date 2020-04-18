"""
tk-lambda.py
"""
from Tkinter import *

def makeLabel(color):
    Label(win2, text='New Label',fg=color,bg='white').pack(side=LEFT)

win1 = Tk()
b1 = Button(win1, text='Blue Label Maker',command=(lambda: makeLabel('blue')))
b2 = Button(win1, text='Green Label Maker',command=(lambda: makeLabel('green')))
b3 = Button(win1, text='Red Label Maker',command=(lambda: makeLabel('red')))
b1.pack()
b2.pack()
b3.pack()
mainloop()
