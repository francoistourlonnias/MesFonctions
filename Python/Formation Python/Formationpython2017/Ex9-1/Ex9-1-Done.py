"""
Exercise 9.1 GUI with Tkinter
"""
# Part A

import airlineClasses
from Tkinter import *
import sqlModule
  
def showReservation(var):
    win3 = Tk()
    btn1 = Button(win3,text='Close',command=win3.destroy)
    btn1.pack(side=TOP)
    reservationId = var.get()
    output = ''
    space = ' '
    nl = '\n'
    reservationInfo = reservationDict[reservationId]
    output = output + str(reservationInfo.reservationId) + space + \
    reservationInfo.name + space + \
    str(reservationInfo.flightData.flightnum) + space + \
    reservationInfo.flightData.departCity + space + reservationInfo.flightData.arriveCity + space + \
    reservationInfo.flightData.departTime + space + reservationInfo.flightData.departDay + space + \
    reservationInfo.flightData.arriveTime + space + reservationInfo.flightData.arriveDay + space + \
    str(reservationInfo.flightData.cost) + space + str(reservationInfo.flightData.code) + nl
    msg1 = Message(win3,text=output)
    msg1.pack()  
    
def showFlights(var):
    win2 = Tk()
    city = var.get()
    output = ''
    space = ' '
    nl = '\n'
    for k in flightDict:
        if flightDict[k].arriveCity == city:
            flightInfo = flightDict[k]
            output = output + str(flightInfo.flightnum) + space + \
            flightInfo.departCity + space + flightInfo.arriveCity + space + \
            flightInfo.departTime + space + flightInfo.departDay + space + \
            flightInfo.arriveTime + space + flightInfo.arriveDay + space + \
            str(flightInfo.cost) + space + str(flightInfo.code) + nl
    msg1 = Message(win2,text=output)
    msg1.pack()

    
# Part B
# create dictionaries here
cityCodeDict = sqlModule.getCityCodeDict()
flightDict = sqlModule.getFlightDict()
reservationDict = sqlModule.getReservationDict()

def layout1():
    win1 = Toplevel()
    
    lab1 = Label(win1,text="Airports")
    lab1.pack()
    
    var = StringVar()
    var.set(' ')
    
    for k in cityCodeDict:
        rb = Radiobutton(win1,text=k,variable=var,value=k,command=(lambda: showFlights(var)))
        rb.pack()
        
    btn1 = Button(win1,text='Exit',command=win1.destroy).pack()

def layout2():
    win2 = Toplevel()
    lab1 = Label(win2,text="Reservations")
    lab1.pack()
    
    var = IntVar()
    var.set(0)
    
    for k in reservationDict:
        rb = Radiobutton(win2,text=k,variable=var,value=k,command=(lambda: showReservation(var)))
        rb.pack()
        
    btn1 = Button(win2,text='Exit',command=win2.destroy).pack()


# Part C

#layout1()
#layout2()

top = Tk()
main=Menu(top)
top.config(menu=main)
m1 = Menu(main)
main.add_cascade(label="Airline Menu",menu=m1)
m1.add_command(label="Flights per city", command=layout1)
m1.add_command(label="Reservation Information",command=layout2)
m1.add_command(label="Exit",command=top.destroy)
mainloop()

