'''
tk-frames.py
'''

from Tkinter import *

class TwoFrames(Frame):
    def __init__(self, labtext, msgtext, msgcolor):
        self.labtext = labtext
        self.msgtext = msgtext
        self.msgcolor = msgcolor

        self.root = Tk()
        Frame.__init__(self)
        self.pack()

        self.leftFrame = Frame(self.root)
        self.leftFrame.pack(side = LEFT)
        self.rightFrame = Frame(self.root)
        self.rightFrame.pack(side = RIGHT)

        self.lab = Label(self.leftFrame, text=self.labtext, fg="purple")
        self.lab.pack()

        self.msg = Message(self.rightFrame, text=self.msgtext, fg=self.msgcolor)
        self.msg.pack(fill=BOTH,expand=YES)

        self.exitBtn = Button(self.leftFrame, text="Exit", fg="red", command=self.root.destroy)
        self.exitBtn.pack(side=BOTTOM)

intro = 'Read this message'
content = '''Line 1 of message
Line 2 of message
Line 3 of message
Line 4 of message
Last line of message'''
gui1 = TwoFrames(labtext=intro, msgtext=content, msgcolor='black')

intro = 'Here is some text'
content = '''Line A of text
Line B of text
Line C has some text
Line D has text too
Line E text
Last line of text?'''
gui2 = TwoFrames(labtext=intro, msgtext=content, msgcolor='blue' )

mainloop()