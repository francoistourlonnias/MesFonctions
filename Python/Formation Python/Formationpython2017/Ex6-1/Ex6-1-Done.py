"""
Exercise 6.1 Modules
"""


import airlineClassesDone

import reservationClass

# Part A

flight1 = airlineClassesDone.Flight( flightnum = 336, departCity = "HKG", arriveCity = "GCM",
                  departTime = "12:00", departDay = "Monday", arriveTime = "20:00",
                  arriveDay = "Monday", cost = 299.99, code = 4 )
flight2 = airlineClassesDone.Flight( flightnum = 337, departCity = "HNL", arriveCity = "ITO",
                  departTime = "8:00", departDay = "Monday", arriveTime = "14:00",
                  arriveDay = "Monday", cost = 199.99, code = 2 )
flight3 = airlineClassesDone.Flight( flightnum = 660, departCity = "CDG", arriveCity = "GCM",
                  departTime = "14:00", departDay = "Monday", arriveTime = "0:00",
                  arriveDay = "Tuesday", cost = 199.99, code = 2 )
flight4 = airlineClassesDone.Flight( flightnum = 681, departCity = "CDG", arriveCity = "ITO",
                  departTime = "6:00", departDay = "Monday", arriveTime = "11:00",
                  arriveDay = "Monday", cost = 209.89, code = 1 )
flight5 = airlineClassesDone.Flight( flightnum = 753, departCity = "LHR", arriveCity = "HKG",
                  departTime = "10:00", departDay = "Monday", arriveTime = "18:00",
                  arriveDay = "Monday", cost = 199.99, code = 2 )

# Part B

flightList = [ flight1, flight2, flight3, flight4, flight5 ]
testFlightDict = {}
for f in flightList:
    airlineClassesDone.genDiscount(f)
    testFlightDict[f.flightnum] = f
    
# Part C

for k in testFlightDict:
    print 'Flight', k, 'cost', testFlightDict[k].cost


# Part D

tmpRes =  reservationClass.Reservation( reservationId = 0, name='Lars Olsen', flightData = flight1 )
print 'Reservation', tmpRes.reservationId, 'for', tmpRes.name, 'on flight', tmpRes.flightData.flightnum


# Part E

name1 = "Pat Holder"
name2 = "Peter Smith"
name3 = "Guy Gildersleeve"
name4 = "Janet Rider"
name5 = "Lynn Jasper"

number = 0

r1 = reservationClass.Reservation(reservationId = number, name = name1, flightData = flight1)
r2 = reservationClass.Reservation(reservationId = number, name = name2, flightData = flight2)
r3 = reservationClass.Reservation(reservationId = number, name = name3, flightData = flight3)
r4 = reservationClass.Reservation(reservationId = number, name = name4, flightData = flight4)
r5 = reservationClass.Reservation(reservationId = number, name = name5, flightData = flight5)

resList = [ r1, r2, r3, r4, r5 ]

reservationDict = {}
for res in resList:
    reservationDict[res.reservationId] = res
    
for k in reservationDict:
    print 'Dictionary reservation', k, reservationDict[k].name,\
        reservationDict[k].flightData.flightnum, reservationDict[k].flightData.cost
        