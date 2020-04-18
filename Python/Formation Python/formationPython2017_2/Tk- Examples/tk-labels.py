"""
tk-labels.py
"""

from Tkinter import *

win1 = Tk()
win2 = Tk()
widget1 = Label(win1, text='Hello')
widget2 = Label(win2, text='World')

widget1.pack()
widget2.pack()
mainloop()


