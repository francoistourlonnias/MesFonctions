"""
Exercise 9.1 GUI with Tkinter
"""
# Part A

import airlineClasses
from Tkinter import *

    
    
# Part B
# create dictionaries here


# create showFlights() here
# 
#

# The coding below builds the concatenated string for display in the message.
# Uncomment these lines to unpack attributes of Airport objects
#
#    output = ''             # initialize variable
#    space = ' '             # assign delimiters
#    nl = '\n'
#    for k in flightDict:                         # loop through the keys
#        if flightDict[k].arriveCity == city:     # test for matching flight
#            flightInfo = flightDict[k]           # construct output string
#            output = output + str(flightInfo.flightnum) + space + \
#           flightInfo.departCity + space + flightInfo.arriveCity + space + \
#            flightInfo.departTime + space + flightInfo.departDay + space + \
#            flightInfo.arriveTime + space + flightInfo.arriveDay + space + \
#            str(flightInfo.cost) + space + str(flightInfo.code) + nl
#
# Use the comments to unpack attributes of Flight objects

# The coding below builds the concatenated string for display in the message.
# Uncomment these lines to unpack attributes of Reservation objects
#
#    output = ''
#    space = ' '
#    nl = '\n'
#    reservationInfo = reservationDict[reservationId]
#    output = output + str(reservationInfo.reservationId) + space + \
#    reservationInfo.name + space + \
#    str(reservationInfo.flightData.flightnum) + space + \
#    reservationInfo.flightData.departCity + space + reservationInfo.flightData.arriveCity + space + \
#    reservationInfo.flightData.departTime + space + reservationInfo.flightData.departDay + space + \
#    reservationInfo.flightData.arriveTime + space + reservationInfo.flightData.arriveDay + space + \
#    str(reservationInfo.flightData.cost) + space + str(reservationInfo.flightData.code) + nl
#
# Use the comments to unpack attributes of Reservation objects


# Part C
def layout1():
    win1 = Toplevel(top)
    
    lab1 = Label(win1,text="Airports")
    lab1.pack()
    
    var = StringVar()
    var.set(' ')
    
    for k in cityCodeDict:
        rb = Radiobutton(win1,text=k,variable=var,value=k,command=(lambda: showFlights(var)))
        rb.pack()
        
    btn1 = Button(win1,text='Exit',command=win1.destroy).pack()

# Part D

top = Tk()

