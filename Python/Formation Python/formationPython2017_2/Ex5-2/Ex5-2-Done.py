"""
Exercise 5.2 Inheritance and Scope
"""
# Part A

class Trip(object):  #rajout de object pour travailler avec super
    def __init__(self, departCity=None, arriveCity=None,
                 departTime=None, departDay=None,
	         arriveTime=None, arriveDay=None):
        self.departCity = departCity
        self.arriveCity = arriveCity
        self.departTime = departTime
        self.departDay = departDay
        self.arriveTime = arriveTime
        self.arriveDay = arriveDay
        
    caribList = [ 'CUR', 'GCM' ]
    hawaiiList = [ 'HNL', 'ITO' ]
    
    def isRoundTrip(self):
        if self.arriveCity == self.departCity and self.departDay == self.arriveDay:
            return True
        else:
            return False

    def isCaribbean(self):
        if self.arriveCity in Trip.caribList:
            return True
        else:
            return False

    def isHawaiian(self):
        if self.arriveCity in Trip.hawaiiList:
            return True
        else:
            return False
  
    def isOverNight(self):
        if self.arriveDay != self.departDay:
            return True
        else:
            return False

    def isInterIsland(self): 
        if self.arriveCity in Trip.hawaiiList and self.departCity in Trip.hawaiiList:
            return True
        else:
            return False

# Part B
# Add the subclass below

class Flight(Trip):
    def __init__(self, flightnum=0, departCity=None, arriveCity=None,
                 departTime=None, departDay=None,
                 arriveTime=None, arriveDay=None,
                 cost=0.0, code=0):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        super(Flight,self).__init__(self,departCity=departCity, arriveCity=arriveCity,
                 departTime=departTime, departDay=departDay,
                 arriveTime=arriveTime, arriveDay=arriveDay)
        
    def discount(self):
        discount = 0.0
        if self.isInterIsland():
            discount += 0.05
        elif self.isHawaiian():
            discount += 0.10
        elif self.isCaribbean():
            discount += 0.15
        self.cost -=  ( self.cost * discount )


# Part C


flight1 = Flight( flightnum = 102, departCity = "HNL", arriveCity = "HKG",
                  departTime = "4:00",departDay = "Monday", arriveTime = "8:00",
                  arriveDay = "Monday", cost = 99.95, code = 4)
flight2 = Flight( flightnum = 204, departCity = "HNL", arriveCity = "ITO",
                  departTime = "8:00", departDay = "Monday", arriveTime = "14:00",
                  arriveDay = "Monday", cost = 199.99, code = 42 )
flight3 = Flight( flightnum = 336, departCity = "HKG", arriveCity = "GCM",
                  departTime = "12:00", departDay = "Monday", arriveTime = "20:00",
                  arriveDay = "Monday", cost = 299.99, code = 44 )
flight4 = Flight( flightnum = 660, departCity = "CDG", arriveCity = "GCM",
                  departTime = "14:00", departDay = "Monday", arriveTime = "0:00",
                  arriveDay = "Tuesday", cost = 199.99, code = 42 )
flight5 = Flight( flightnum = 681, departCity = "CDG", arriveCity = "ITO",
                  departTime = "6:00", departDay = "Monday", arriveTime = "11:00",
                  arriveDay = "Monday", cost = 209.89, code = 41 )
flight6 = Flight( flightnum = 753, departCity = "LHR", arriveCity = "HKG",
                  departTime = "10:00", departDay = "Monday", arriveTime = "18:00",
                  arriveDay = "Monday", cost = 199.99, code = 42 )


flightList = [ flight1, flight2, flight3, flight4, flight5, flight6 ]
for f in flightList:
    print 'Before discount', f.flightnum, f.cost
    f.discount()
    print 'After discount', f.flightnum, f.cost
    
# Part D

def nextId(number):
    while True:
        number = number + 1
        yield number

    
num = nextId(99)

class Reservation():
    def __init__(self, reservationId, name,
                 flightData):
        self.reservationId = next(num)
        self.name = name
        self.flightData = flightData

number = 0
name1 = "Pat Holder"
name2 = "Peter Smith"
name3 = "Guy Gildersleeve"
name4 = "Janet Rider"
name5 = "Lynn Jasper"
name6 = "Ian Rouselle"

r1 = Reservation(reservationId = number, name = name1, flightData = flight1)
r2 = Reservation(reservationId = number, name = name2, flightData = flight2)
r3 = Reservation(reservationId = number, name = name3, flightData = flight3)
r4 = Reservation(reservationId = number, name = name4, flightData = flight4)
r5 = Reservation(reservationId = number, name = name5, flightData = flight5)
r6 = Reservation(reservationId = number, name = name6, flightData = flight6)
print "Reservation", r1.reservationId, r1.name, r1.flightData.flightnum, r1.flightData.cost
print "Reservation", r2.reservationId, r2.name, r2.flightData.flightnum, r2.flightData.cost
print "Reservation", r3.reservationId, r3.name, r3.flightData.flightnum, r3.flightData.cost
print "Reservation", r4.reservationId, r4.name, r4.flightData.flightnum, r4.flightData.cost
print "Reservation", r5.reservationId, r5.name, r5.flightData.flightnum, r5.flightData.cost
print "Reservation", r6.reservationId, r6.name, r6.flightData.flightnum, r6.flightData.cost