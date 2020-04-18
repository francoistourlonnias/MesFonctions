"""
tk-msg.py
"""
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

from Tkinter import *

def showAirportCode():
    t1 = Tk()
    output=''
    for key in cityCodeDict:
        output = output  + ' ' + key
    Message(t1, text=output).pack(side=TOP,expand=YES,fill=X)
    Button(t1, text='Exit',command=t1.destroy).pack(side=BOTTOM)
    
def showAirportName():
    t1 = Tk()
    output=''
    for key in cityCodeDict:
        output = output + ' ' + cityCodeDict[key]
    Message(t1, text=output).pack(side=TOP)
    Button(t1, text='Press to exit',command=t1.destroy).pack(side=BOTTOM)        

win1 = Tk()
b1 = Button(win1, text='Press to display airport name',command=showAirportName)
b2 = Button(win1, text='Press to display airport code',command=showAirportCode)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
mainloop()
