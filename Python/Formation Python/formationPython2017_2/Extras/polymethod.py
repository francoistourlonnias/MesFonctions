class Trip:
    def __init__(self, departDay, arriveDay):
        self.departDay = departDay
        self.arriveDay = arriveDay
    def printTrip(self):
        print 'Schedule is', self.departDay, self.arriveDay,
              
class Cruise(Trip):
    def __init__(self, departDay, arriveDay, vessel='Minnow'):
        self.vessel = vessel
        Trip.__init__(self,departDay, arriveDay)
    def printTrip(self):
        Trip.printTrip(self)
        print 'Ship is', self.vessel
        
class Train(Trip):
    def __init__(self, departDay, arriveDay, cost=0.0):
        self.cost = cost
        Trip.__init__(self, departDay, arriveDay)
    def printTrip(self):
        Trip.printTrip(self)
        print 'Cost is %7.2f' % self.cost
    
myTrip = Cruise(departDay='Friday', arriveDay='Saturday', vessel="Moonbeam")
yourTrip = Train(departDay='Wednesday', arriveDay='Friday', cost=250.0)
myTrip.printTrip()
yourTrip.printTrip()
