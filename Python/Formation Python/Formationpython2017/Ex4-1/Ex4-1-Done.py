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

def listAllCities():
    for k in cityCodeDict:
        print 'Airport code', k, 'Airport name', cityCodeDict[k]

def flightsPerCity(dict,apt):
    for key in dict:
        if dict[key][0] == apt:
            print 'Flight', key, 'on the schedule', dict[key]
            
def flightsPerCities(dict,departApt,arriveApt):
    outList = []
    for key in dict:
        if dict[key][0] == departApt and dict[key][1] == arriveApt:
            outList.append(key)

    return outList
            

# Part B

print 'The list of airport codes and airports is'

listAllCities()

searchCity = 'HNL'
print 'The flights to', searchCity
flightsPerCity(flightDict, searchCity)

searchCity = 'CUR'
print 'The flights to', searchCity
flightsPerCity(flightDict, searchCity)

searchCity = 'ITO'
print 'The flights to', searchCity
flightsPerCity(flightDict, searchCity)


departCity = 'NRT'
arriveCity = 'ITO'
print 'The flights from', departCity, 'to', arriveCity


flightList = flightsPerCities(flightDict, departCity, arriveCity)

for x in flightList:
    print x

departCity = 'HKG'
arriveCity = 'HNL'
print 'The flights from', departCity,'to', arriveCity
flightList = flightsPerCities(dict=flightDict, departApt=departCity, arriveApt=arriveCity)
for x in flightList:
    print x
    
def ctof(input):
    freezing = 32
    output = input * 9.0 / 5.0 + freezing
    return output

def ftoc(input):
    freezing = 32
    output = ( input - freezing ) * 5.0 / 9.0
    return output

Paris = 25
Honolulu = 81

print 'Temperature in Paris in C is', Paris
print 'Temperature in Paris in F is', ctof(Paris)

print 'Temperature in Honolulu in F is', Honolulu
print 'Temperature in Honolulu in C is', ftoc(Honolulu)

def discount(price, disc):
    return price - ( price * disc )

price = 100
disc =  0.05
newprice = discount(price,disc)
print 'Original = ', price, 'discount = ', disc, 'discounted = ', newprice

price = 299
disc =  0.15
newprice = discount(price,disc)
print 'Original = ', price, 'discount = ', disc, 'discounted = ', newprice


price = 399.95
disc = 0.10
newprice = discount(price,disc)
print 'Original = ', price, 'discount = ', disc, 'discounted = ', newprice


