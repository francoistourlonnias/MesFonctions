"""
Exercise 3.1 Collections and Looping
"""

# Part A
codeList = ['HNL','ITO','LHR','LGA','GCM','MSY','LAX']



flightList = ['HNL','HKG','4:00','Monday','8:00','Monday','99.95',4]
# flightList = [ departCity, arriveCity, departTime, departDay,
#                arriveTime, arriveDay, cost, code ]


# Part B

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



# Part C
codeList = ['HNL','ITO','LHR','LGA','GCM','MSY']

flightList = ['HNL','HKG','4:00','Monday','8:00','Monday','99.95',4]


# Part D

flightDict = {
    102:['HNL','HKG','4:00','Monday','8:00','Monday','99.95',4],
    132:['HNL','HNL','4:00','Monday','8:00','Monday','59.0',2],
    276:['HKG','CDG','15:00','Monday','3:00','Tuesday','233.99',2],
    303:['HKG','ARN','9:00','Monday','16:00','Monday','233.99',2],
    498:['NRT','ITO','14:00','Monday','0:00','Tuesday','159.99',2],
    390:['CUR','CUR','4:00','Thursday','8:00','Thursday','599.95',3],
    465:['NRT','YYZ','4:00','Thursday','8:00','Thursday','59.0',3],
    1305:['ITO','ARN','4:00','Thursday','8:00','Thursday','125.0',2],
    375:['HKG','HNL','6:00','Friday','11:00','Friday','299.99',4],
    444:['NRT','LHR','15:00','Friday','3:00','Saturday','125.0',3],
    1572:['HNL','HNL','4:00','Sunday','8:00','Sunday','125.0',2] }

