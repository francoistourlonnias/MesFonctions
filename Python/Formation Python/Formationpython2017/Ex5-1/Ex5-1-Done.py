"""
Exercise 5.1 Classes and Initialization
"""
# Part A

class Aircraft:
    def __init__(self, code=0, name=None):
        self.code = code
        self.name = name


class Airport:
    def __init__(self, cityCode=None, city=None):
        self.cityCode = cityCode
        self.city = city

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

# Sample data for Trip
depCity = 'CUR'
arrCity = 'HNL'
depTime = '12:00'
depDay = 'Sunday'
arrTime = '20:00'
arrDay = 'Sunday'

sampleTrip = Trip(departCity=depCity,arriveCity=arrCity,
            departTime=depTime, departDay=depDay, arriveTime=arrTime, arriveDay=arrDay)


print 'sampleTrip', sampleTrip.departCity, sampleTrip.arriveCity,\
      sampleTrip.departTime, sampleTrip.departDay,\
      sampleTrip.arriveTime, sampleTrip.arriveDay
      
print 'The Trip caribList is', Trip.caribList
print 'The Trip hawaiiList is ', Trip.hawaiiList
        
                        
# Part B


trip1 = Trip(departCity="HNL",arriveCity="ITO",departTime="8:00",departDay="Monday",
             arriveTime="14:00",arriveDay="Monday")
trip2 = Trip(departCity="HKG",arriveCity="HNL",departTime="6:00",departDay="Monday",
             arriveTime="11:00",arriveDay="Monday")
trip3 = Trip(departCity="CDG",arriveCity="GCM",departTime="12:00",departDay="Monday",
             arriveTime="20:00",arriveDay="Monday")
trip4 = Trip(departCity="ARN",arriveCity="CDG",departTime="17:00",departDay="Tuesday",
             arriveTime="7:00",arriveDay="Wednesday")

print 'Trip test', trip1.departCity, trip2.departCity, trip3.departCity, trip4.departCity

tripList = [ trip1, trip2, trip3, trip4 ]
def printTrip(t):
    print t.departCity, t.arriveCity, t.departTime, t.departDay, t.arriveTime, t.arriveDay
    
for t in tripList:
    if t.isRoundTrip():
        printTrip(t)
        print 'is RoundTrip'
    if t.isCaribbean():
        printTrip(t)
        print 'is Caribbean'
    if t.isHawaiian():
        printTrip(t)
        print 'is Hawaiian'
    if t.isOverNight():
        printTrip(t)
        print 'is Overnight'
    if t.isInterIsland():
        printTrip(t)
        print 'is Interisland'

# Part C
      
# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# city is Honolulu

sampleAircraft = Aircraft(code=1, name='Canadian Regional Jet')
sampleAirport = Airport(cityCode='HNL', city='Honolulu')
print 'sampleAircraft', sampleAircraft.code, sampleAircraft.name
print 'sampleAirport', sampleAirport.cityCode, sampleAirport.city
