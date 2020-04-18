"""
Exercise 4.1 Creating and Calling Functions
"""
# Data for the exercise
# Please do not modify these dictionaries

# Data description of cityCodeDict
#    Airport Code : Airport Name

cityCodeDict = {
    'HNL':'Honolulu',
    'ITO':'Hilo',
    'LHR':'London/Heathrow',
    'ARN':'Stockholm/Arlanda',
    'HKG':'Hong Kong',
    'YYZ':'Toronto',
    'CDG':'Paris/Charles De Gaulle',
    'NRT':'Tokyo/Narita',
    'GCM':'Grand Cayman BWI',
    'CUR':'Curacao Netherland Antilles' }

# Data description of flightDict
#    Flight Number : flightList
# flightList = [ departCity, arriveCity, departTime, departDay,
#                arriveTime, arriveDay, cost, code ]


flightDict = {
    102:['HNL','HKG','4:00','Monday','8:00','Monday','99.95',4],
    132:['HNL','HNL','4:00','Monday','8:00','Monday','59.0',2],
    276:['HKG','CDG','15:00','Monday','3:00','Tuesday','233.99',2],
    303:['HKG','ARN','9:00','Monday','16:00','Monday','233.99',2],
    498:['NRT','ITO','14:00','Monday','0:00','Tuesday','159.99',2],
    390:['HKG','CUR','4:00','Thursday','8:00','Thursday','599.95',3],
    465:['NRT','YYZ','4:00','Thursday','8:00','Thursday','59.0',3],
    1305:['ITO','ARN','4:00','Thursday','8:00','Thursday','125.0',2],
    375:['HKG','HNL','6:00','Friday','11:00','Friday','299.99',4],
    444:['NRT','LHR','15:00','Friday','3:00','Saturday','125.0',3],
    1572:['CUR','HNL','4:00','Sunday','8:00','Sunday','125.0',2] }



# Part A 
def bizarre(myliste=[]):
    myliste.append(42)
    return myliste

#appel
bizarre()
madata=[1,2,3]
bizare(madata)


def bizarre(myliste=[()]): #antidote
    myliste.append(42)
    return myliste

def list_all_cities():
    for i in cityCodeDict:
        print 'Airport code', i, 'Airport name', cityCodeDict[i]

print "fts "
list_all_cities()

# Part B 

searchCity = 'HNL'


searchCity = 'CUR'


searchCity = 'ITO'


# Part C Calling

departCity = 'NRT'
arriveCity = 'ITO'


