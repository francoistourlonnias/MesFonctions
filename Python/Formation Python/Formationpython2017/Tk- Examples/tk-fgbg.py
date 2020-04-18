"""
tk-fgbg.py
"""

from Tkinter import *

win1 = Tk()
win2 = Tk()
widget1 = Label(win1, text='Hello',fg='blue',bg='white')
widget2 = Label(win1, text='World',fg='white',bg='blue')

widget1.pack()
widget2.pack()
mainloop()


