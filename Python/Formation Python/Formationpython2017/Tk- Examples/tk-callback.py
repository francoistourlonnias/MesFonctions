"""
tk-callback
"""
from Tkinter import *

def makeLabel():
    Label(win1, text='New Label').pack(side=BOTTOM)

win1 = Tk()
b1 = Button(win1, text='Label Maker',command=makeLabel)
b1.pack(side=TOP)
mainloop()
