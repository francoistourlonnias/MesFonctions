"""
airlineClasses module
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

    def isCarribean(self):
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
        Trip.__init__(self,departCity, arriveCity,
                 departTime, departDay,
                 arriveTime, arriveDay)
        
    def discount(self):
        discount = 0.0
        if self.isInterIsland():
            discount += 0.05
        elif self.isHawaiian():
            discount += 0.10
        elif self.isCarribean():
            discount += 0.15
        self.cost -=  ( self.cost * discount )

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

class Aircraft:
    def __init__(self, aircraftCode=0, name=None):
        self.aircraftCode = aircraftCode
        self.name = name
        
class Airport:
    def __init__(self, cityCode=None, city=None):
        self.cityCode = cityCode
        self.city = city
