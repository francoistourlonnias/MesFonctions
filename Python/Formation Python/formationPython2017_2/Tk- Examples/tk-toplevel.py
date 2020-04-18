"""
tk-toplevel.py
"""

from Tkinter import *

win1 = Tk()
win1.title('Parent')
win2 = Toplevel(win1)
win2.title('Child')
mainloop()


