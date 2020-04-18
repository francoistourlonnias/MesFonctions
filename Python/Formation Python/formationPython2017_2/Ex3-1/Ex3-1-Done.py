"""
Exercise 3.1 Collections and Looping
"""

# Part A
codeList = ['HNL','ITO','LHR','LGA','GCM','MSY','LAX']

print 'The first two city codes are', codeList[:2]
print 'The last two city codes are', codeList[- 2:]


flightList = ['HNL','HKG','4:00','Monday','8:00','Monday','99.95',4]
# The elements of the list map to these values
# flightList = [ departCity, arriveCity, departTime, departDay,
#                arriveTime, arriveDay, cost, code ]

departCity = flightList[0]
arriveCity = flightList[1]
departTime = flightList[2]
departDay = flightList[3]
arriveTime = flightList[4]
arriveDay = flightList[5]
price = flightList[6]
code = flightList[7]

print 'Using slicing'
print 'The flight travels from', departCity, 'to', arriveCity
print 'The flight departs on', departDay, 'and arrives on', arriveDay

departCity, arriveCity, departTime, departDay, arriveTime, arriveDay, price, code = flightList

print 'Using sequence unpacking'
print 'The flight travels from', departCity, 'to', arriveCity
print 'The flight departs on', departDay, 'and arrives on', arriveDay

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
    'CUR':'Curaca, Netherland Antilles' }

print 'The airport codes'
for k in cityCodeDict.keys():
    print k

print 'The airport names'
for v in cityCodeDict.values():
    print v

print 'Keys and values without a method'
for v in cityCodeDict:
    print v, cityCodeDict[v]
# Part C

codeList = ['HNL','ITO','LHR','LGA','GCM','MSY']

print 'The cities in the list we do not serve'
print [ x for x in codeList if x not in cityCodeDict.keys() ]

print 'The cities in the list we do serve'
print [ x for x in codeList if x in cityCodeDict.keys() ]

codeListSet = set(codeList)
cityCodeDictSet = set(cityCodeDict.keys())

print 'The cities in the list we do not serve by set', list(codeListSet - cityCodeDictSet)
print 'The cities in the list we do serve by set', list(codeListSet & cityCodeDictSet)

flightList = ['HNL','HKG','4:00','Monday','8:00','Monday','99.95',4]

departCity = flightList[0]
arriveCity = flightList[1]
if departCity in cityCodeDict.keys() and arriveCity in cityCodeDict.keys():
    print 'We fly from', departCity, 'to', arriveCity
else:
    print 'We do not fly from', departCity, 'to', arriveCity


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


for k in flightDict:
    
    departCity,arriveCity,departTime,departDay,arriveTime,arriveDay,price,code = flightDict[k]

    if departDay != arriveDay:
        print 'The overnight flights are', k

    if departCity == arriveCity:
        print 'The round trip flights are', k
        

roundTripList = []
overNightList = []
for k in flightDict:
    
    departCity,arriveCity,departTime,departDay,arriveTime,arriveDay,price,code = flightDict[k]

    if departDay != arriveDay:
        overNightList.append(k)

    if departCity == arriveCity:
        roundTripList.append(k)

print 'The over night list is', overNightList
print 'The round trip list is', roundTripList
