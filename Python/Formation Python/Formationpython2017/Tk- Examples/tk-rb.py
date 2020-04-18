"""
tk-rb.py
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

#def showAirport(code):
def showAirport():
    t1 = Tk()
    code=var.get()
    airport = cityCodeDict[code]
    Label(t1, text=airport).pack(side=TOP)
    butn1 = Button(t1, text='Press to exit',command=t1.destroy)
    butn1.pack(side=BOTTOM)


 
def makeRadio(window,code):
    #var=StringVar()
    rb = Radiobutton(win1,text=code,variable=var,value=code,command=lambda: showAirport(code))
    rb.pack()
    
win1 = Tk()

Label(win1, text='Select Airport Code below').pack(side=TOP)

var=StringVar()
var.set(' ')

for k in cityCodeDict:
    #makeRadio(win1,k)
 #   rb = Radiobutton(win1,text=k,variable=var,value=k,command=lambda code=k: showAirport(code))
    #var=k
    rb = Radiobutton(win1,text=k,variable=var,value=k,command=showAirport)
    rb.pack()  

mainloop()
