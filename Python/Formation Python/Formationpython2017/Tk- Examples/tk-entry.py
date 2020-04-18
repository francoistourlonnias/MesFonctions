"""
tk-entry.py
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

def getDictKeys(dictionary):
    output=''
    for key in dictionary:
        output = output + '\n' + key
    return output

def showAirport():
    t1 = Tk()
    code = ent1.get()
    codeUp = code.upper()
    if codeUp in cityCodeDict:
        airport = cityCodeDict[codeUp]
    else:
        airport = code + ' is not a valid airport code'
    ent1.delete(0,END)
    Label(t1, text=airport).pack(side=TOP)
    butn1 = Button(t1, text='Press to exit',command=t1.destroy)
    butn1.pack(side=BOTTOM)

win1 = Tk()
output = getDictKeys(cityCodeDict)
lab1 = Label(win1, text=output)
lab2 = Label(win1, text='Enter Airport Code below')
ent1 = Entry(win1)
b1 = Button(win1, text='Press to display',command=showAirport)
lab1.pack(side=TOP)
lab2.pack(side=TOP)
ent1.pack(side=TOP)
b1.pack(side=TOP)

mainloop()
