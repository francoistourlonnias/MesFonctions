"""
Exercise 5.1 Classes and Initialization
"""
# Part A

# Sample data for Trip
depCity = 'CUR'
arrCity = 'HNL'
depTime = '12:00'
depDay = 'Sunday'
arrTime = '20:00'
arrDay = 'Sunday'



# Part B
caribList = [ 'GCM', 'CUR' ]
hawaiiList = [ 'ITO', 'HNL' ]

trip1 = Trip(departCity="HNL",arriveCity="ITO",departTime="8:00",departDay="Monday",
             arriveTime="14:00",arriveDay="Monday")
trip2 = Trip(departCity="HKG",arriveCity="HNL",departTime="6:00",departDay="Monday",
             arriveTime="11:00",arriveDay="Monday")
trip3 = Trip(departCity="CDG",arriveCity="GCM",departTime="12:00",departDay="Monday",
             arriveTime="20:00",arriveDay="Monday")
trip4 = Trip(departCity="ARN",arriveCity="CDG",departTime="17:00",departDay="Tuesday",
             arriveTime="7:00",arriveDay="Wednesday")

#tripList = [ trip1, trip2, trip3, trip4 ]
#def printTrip(t):
#    print t.departCity, t.arriveCity, t.departTime, t.departDay, t.arriveTime, t.arriveDay


# Part C

# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# city is Honolulu
