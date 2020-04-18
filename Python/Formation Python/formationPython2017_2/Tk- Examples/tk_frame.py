"""
tk-frame.py
"""

from Tkinter import *

cityCodeDict = {
    'HNL':'Honolulu',
    'ITO':'Hilo',
    'LHR':'London/Heathrow',
    'ARN':'Stockholm/Arlanda',
    'HKG':'Hong Kong',
    'YYZ':'Toronto',
    'CDG':'Paris/Charles De Gaulle',
    'NRT':'Tokyo/Narita',
    'GCM':'Grand Cayman, BWI',
    'CUR':'Curacao, Netherland Antilles' }


flightDict = {
    102:['HNL','HKG','4:00','Monday','8:00','Monday','99.95',4],
    132:['HNL','HNL','4:00','Monday','8:00','Monday','59.0',2],
    276:['HKG','CDG','15:00','Monday','3:00','Tuesday','233.99',2],
    303:['HKG','ARN','9:00','Monday','16:00','Monday','233.99',2],
    498:['NRT','ITO','14:00','Monday','0:00','Tuesday','159.99',2],
    390:['HKG','CUR','4:00','Thursday','8:00','Thursday','599.95',3],
    465:['NRT','YYZ','4:00','Thursday','8:00','Thursday','59.0',3],
    1305:['ITO','ARN','4:00','Thursday','8:00','Thursday','125.0',2],
    375:['HKG','HNL','6:00','Friday','11:00','Friday','299.99',4],
    444:['NRT','LHR','15:00','Friday','3:00','Saturday','125.0',3],
    1572:['CUR','HNL','4:00','Sunday','8:00','Sunday','125.0',2] }


class DictLayout(Frame):
    def __init__(self,title,dict):
        self.title=title
        #parent = Tk()

        Frame.__init__(self)
        self.pack()
        self.dict=dict
        self.var=StringVar()
        self.var.set(' ')

        self.leftFrame=Frame(self).pack(side=LEFT)
        self.rightFrame=Frame(self).pack(side=RIGHT)
        self.makeLayout()

    def showValue(self):
        self.output=''
        self.output=self.dict[self.var.get()]
        Message(self.rightFrame,text=self.output).pack(side=BOTTOM)
           
    def makeLayout(self):
        lab1 = Label(self.leftFrame,text=self.title).pack(side=TOP)
        for k in self.dict:
            Radiobutton(self.rightFrame,text=k,variable=self.var,value=k,command=self.showValue).pack(side=TOP)

        btn1 = Button(self.leftFrame,text='Exit',command=self.destroy)
        btn1.pack(side=BOTTOM)


     
#win1 = Toplevel()
gui1 = DictLayout(title='Airports',dict=cityCodeDict)
#win2 = Toplevel()
#gui2 = IntDictLayout(title='Flights',dict=flightDict)
import sys

mainloop()
#print 'go'
#sys.stdin.readline()
