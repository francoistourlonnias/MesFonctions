"""
tk-menu.py
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

def showDictValues(dictionary):
    output=''
    for key in dictionary:
        output = output + '\n' + str(dictionary[key])

    top2 = Tk()
    msg = Message(top2, text=output)
    msg.pack(side=TOP)
    btn = Button(top2, text='Press to close',command=top2.destroy)
    btn.pack(side=BOTTOM)
    
def showDictKeys(dictionary):
    output=''
    for key in dictionary:
        output = output + '\n' + key

    top2 = Tk()
    msg = Message(top2, text=output)
    msg.pack(side=TOP)
    btn = Button(top2, text='Press to close',command=top2.destroy)
    btn.pack(side=BOTTOM)

def showAirport(code):
    output=cityCodeDict[code]
    top2 = Tk()
    lab = Label(top2, text=output)
    lab.pack(side=TOP)
    btn = Button(top2, text='Press to close',command=top2.destroy)
    btn.pack(side=BOTTOM) 
    
def addMenu(menu,code):
    menu.add_command(label=code,command=lambda: showAirport(code))
    
top1 = Tk()
mainmenu = Menu(top1)
top1.config(menu=mainmenu)

airportMenu = Menu(mainmenu)
airportInfo = Menu(airportMenu)
airportSel = Menu(airportMenu)
mainmenu.add_cascade(label='Airport Menu', menu=airportMenu)
airportMenu.add_cascade(label='Airport Information',menu=airportInfo)
airportInfo.add_cascade(label='Airport Selection',menu=airportSel)

airportMenu.add_command(label='Exit', command=top1.destroy)
airportInfo.add_command(label='Airport Names', command=lambda: showDictValues(cityCodeDict))
airportInfo.add_command(label='Airport Codes', command=lambda: showDictKeys(cityCodeDict))

for key in cityCodeDict:
    addMenu(airportSel,key)
    
mainloop()
