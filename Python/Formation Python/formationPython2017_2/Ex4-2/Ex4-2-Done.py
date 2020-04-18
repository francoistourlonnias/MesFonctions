"""
Exercise 4.2 Lambda Functions and Generators
"""
# Part A

Paris = 25
Honolulu = 81

# Create lambda functions below

#ici les lambda permettent de gagner un ligne c'est peu !!!!!!!
freezing = 32
ctof = lambda x: x * 9.0 / 5.0 + freezing
ftoc = lambda x: ( x - freezing ) * 5.0 / 9.0

print 'Paris is', ctof(Paris)
print 'Honolulu is', ftoc(Honolulu)

# Part B

caribList = [ 'GCM', 'CUR' ]
cityList = [ 'HNL', 'CDG', 'MSY', 'CUR', 'HKG', 'YYZ', 'ARN', 'GPT' ]

# Create lambda function below

inList = lambda value, airportList: value in airportList
for apt in cityList:
    if inList(apt, caribList):
        print apt, 'is in', caribList
    else:
        print apt, 'is not in', caribList
        
# Part C
#GENERATEUR!!!!!!!!!!!!!!!!!!!!!!!!
def nextId(number):
    while True:
        number = number + 1
        yield number

result = nextId(99)
for num in range(1,10):
    print next(result)

# Part D   

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

cityList = [ 'HNL', 'CDG', 'MSY', 'CUR', 'HKG', 'YYZ', 'ARN', 'GPT' ]

inDict = lambda apt, dict: apt in dict.keys()

for apt in cityList:
    if inDict(apt,cityCodeDict):
        print apt, 'is a key for', cityCodeDict[apt]
    else:
        print apt, 'is not in the dictionary'

        
# Part E

hawaiiList = [ 'ITO', 'HNL' ]
euroList =  [ 'LHR', 'CDG' ] 
asiaList = [ 'HKG', 'NRT' ]

for apt in cityList:
    if inList(apt, hawaiiList):
        print apt, 'is within hawaiiList'
    elif inList(apt, euroList):
        print apt, 'is within euroList'
    elif inList(apt, asiaList):
        print apt, 'is within asiaList'
    else:
        print apt, 'is not within any list'
        

