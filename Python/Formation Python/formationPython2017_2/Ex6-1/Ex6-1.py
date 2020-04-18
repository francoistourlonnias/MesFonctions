"""
Exercise 6.1 Modules
"""
# Part A


flight1 = ( flightnum = 336, departCity = "HKG", arriveCity = "GCM",
                  departTime = "12:00", departDay = "Monday", arriveTime = "20:00",
                  arriveDay = "Monday", cost = 299.99, code = 4 )
flight2 = ( flightnum = 337, departCity = "HNL", arriveCity = "ITO",
                  departTime = "8:00", departDay = "Monday", arriveTime = "14:00",
                  arriveDay = "Monday", cost = 199.99, code = 2 )
flight3 = ( flightnum = 660, departCity = "CDG", arriveCity = "GCM",
                  departTime = "14:00", departDay = "Monday", arriveTime = "0:00",
                  arriveDay = "Tuesday", cost = 199.99, code = 2 )
flight4 = ( flightnum = 681, departCity = "CDG", arriveCity = "ITO",
                  departTime = "6:00", departDay = "Monday", arriveTime = "11:00",
                  arriveDay = "Monday", cost = 209.89, code = 1 )
flight5 = ( flightnum = 753, departCity = "LHR", arriveCity = "HKG",
                  departTime = "10:00", departDay = "Monday", arriveTime = "18:00",
                  arriveDay = "Monday", cost = 199.99, code = 2 )


# Part B

flightList = [ flight1, flight2, flight3, flight4, flight5 ]
for flight in flightList:
    pass

# Part C



# Part D

tmpRes =  ( reservationId = 0, name='Lars Olsen', flightData = flight1 )


# Part E

name1 = "Pat Holder"
name2 = "Peter Smith"
name3 = "Guy Gildersleeve"
name4 = "Janet Rider"
name5 = "Lynn Jasper"

number = 0

r1 = (reservationId = number, name = name1, flightData = flight1)
r2 = (reservationId = number, name = name2, flightData = flight2)
r3 = (reservationId = number, name = name3, flightData = flight3)
r4 = (reservationId = number, name = name4, flightData = flight4)
r5 = (reservationId = number, name = name5, flightData = flight5)

resList = [ r1, r2, r3, r4, r5 ]
