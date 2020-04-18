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
       
def genDiscount(obj):
    if isinstance(obj,Flight):
        Flight.discount(obj)
    elif isinstance(obj,Cruise):
        Cruise.discount(obj)
    else:
        print 'object is not a Flight or Cruise'
