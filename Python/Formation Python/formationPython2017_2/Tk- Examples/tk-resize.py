"""
tk-resize.py
"""

from Tkinter import *

win1 = Tk()
win2 = Tk()
widget1 = Label(win1, text='Hello',fg='blue',bg='white')
widget2 = Label(win2, text='World',fg='white',bg='pink')

widget1.pack(fill=X,expand=YES)
widget2.pack(fill=Y,expand=YES)
mainloop()


