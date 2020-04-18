"""
tk-grid.py
"""

from Tkinter import *

win1 = Tk()
Label(win1, text='grid').grid(column=0,row=0)
Label(win1, text='more').grid(column=0,row=1)
Label(win1, text='for').grid(column=0,row=2)

Label(win1, text='provides').grid(column=1,row=0)
Label(win1, text='control').grid(column=1,row=1)
Label(win1, text='tables').grid(column=1,row=2)

mainloop()


