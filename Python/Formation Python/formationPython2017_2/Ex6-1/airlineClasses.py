"""
Exercise 6.1 airlineClasses
"""

class Trip:
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


class Flight(Trip):
    def __init__(self, flightnum=0, departCity=None, arriveCity=None,
                 departTime=None, departDay=None,
                 arriveTime=None, arriveDay=None,
                 cost=0.0, code=0):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        Trip.__init__(self,departCity=departCity, arriveCity=arriveCity,
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

# Part A

class Cruise(Trip):
    def __init__(self, cruisenum=0, departCity=None, arriveCity=None,
                 departTime=None, departDay=None,
                 arriveTime=None, arriveDay=None,
                 cost=0.0, code=0):
        self.cruisenum = cruisenum
        self.cost = cost
        self.code = code
        Trip.__init__(self,departCity, arriveCity,
                 departTime, departDay,
                 arriveTime, arriveDay)

    def discount(self):
        discount = 0
        if self.isInterIsland():
            discount += 0.10
        elif self.isHawaiian():
            discount += 0.20
        self.cost -=  ( self.cost * discount )
        
# Part B

cruise1 = Cruise( cruisenum = 201, departCity = "HNL", arriveCity = "ITO",
                  departTime = "08:00", departDay = "Monday",arriveTime = "23:00",
                  arriveDay = "Monday", cost = 199.99, code = "I" )
flight1 = Flight( flightnum = 336, departCity = "HKG", arriveCity = "GCM",
                  departTime = "12:00", departDay = "Monday", arriveTime = "20:00",
                  arriveDay = "Monday", cost = 299.99, code = 4 )

print 'Before discount cruise', cruise1.cruisenum, cruise1.departCity, cruise1.arriveCity, cruise1.cost
print 'Before discount flight', flight1.flightnum, flight1.departCity, flight1.arriveCity, flight1.cost
cruise1.discount()
flight1.discount()
print 'After discount cruise', cruise1.cruisenum, cruise1.departCity, cruise1.arriveCity, cruise1.cost
print 'After discount flight', flight1.flightnum, flight1.departCity, flight1.arriveCity, flight1.cost

# Part C

def genDiscount(obj):
    if isinstance(obj,Flight):
        Flight.discount(obj)
    elif isinstance(obj,Cruise):
        Cruise.discount(obj)
    else:
        print 'object is not a Flight or Cruise'

cruise2 = Cruise( cruisenum = 202, departCity = "HNL", arriveCity = "ITO",
                  departTime = "05:00", departDay = "Sunday", arriveTime = "21:30",
                  arriveDay = "Sunday", cost = 99.99, code = "O" )
flight2 = Flight( flightnum = 337, departCity = "HNL", arriveCity = "ITO",
                  departTime = "8:00", departDay = "Monday", arriveTime = "14:00",
                  arriveDay = "Monday", cost = 199.99, code = 2 )
        
print 'Before genDiscount cruise', cruise2.cruisenum, cruise2.departCity, cruise2.arriveCity, cruise2.cost
print 'Before genDiscount flight', flight2.flightnum, flight2.departCity, flight2.arriveCity, flight2.cost
genDiscount(cruise2)
genDiscount(flight2)
print 'After genDiscount cruise', cruise2.cruisenum, cruise2.departCity, cruise2.arriveCity, cruise2.cost
print 'After genDiscount flight', flight2.flightnum, flight2.departCity, flight2.arriveCity, flight2.cost

# Part D
