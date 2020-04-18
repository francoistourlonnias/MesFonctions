"""
Exercise 9.1 GUI with Tkinter
"""
# Part A

import airlineClasses
from Tkinter import *

import sqlModule

# Part B
# create dictionaries here

cityCodeDict = sqlModule.getCityCodeDict()
flightDict = sqlModule.getFlightDict()
reservationDict = sqlModule.getReservationDict()


def showFlights(var):
    win2 = Tk()
    
    scrollbar = Scrollbar(win2)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    city = var.get()
    output = ''
    space = ' '
    
    lb1 = Listbox(win2,yscrollcommand=scrollbar.set)
    
    for k in flightDict:
        if flightDict[k].arriveCity == city:
            flightInfo = flightDict[k]
            output = str(flightInfo.flightnum) + space + \
            flightInfo.departCity + space + flightInfo.arriveCity + space + \
            flightInfo.departTime + space + flightInfo.departDay + space + \
            flightInfo.arriveTime + space + flightInfo.arriveDay + space + \
            str(flightInfo.cost) + space + str(flightInfo.code)
            
            lb1.insert(END,output)

    
    lb1.pack(fill=BOTH,expand=YES)
    scrollbar.config(command=lb1.yview)

# Part C

def layout1():
    win1 = Tk()
    
    lab1 = Label(win1,text="Airports")
    lab1.pack()
    
    var = StringVar()
    var.set(' ')
    
    for k in cityCodeDict:
        rb = Radiobutton(win1,text=k,variable=var,value=k,command=(lambda: showFlights(var)))
        rb.pack()
        
    btn1 = Button(win1,text='Exit',command=win1.destroy).pack()

# Part D


layout1()
mainloop()


