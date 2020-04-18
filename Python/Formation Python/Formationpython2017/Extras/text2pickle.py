"""
Prepare data files for Hands On 7.1b
Create the pickle files from the csv files
"""
# Part A

# For the first part of the exercise.
# Use these files to access the .csv data
filename1 = 'C:/Course/1905/Data/airports.csv'
filename2 = 'C:/Course/1905/Data/aircraft.csv'
filename3 = 'C:/Course/1905/Data/flights.csv'



# Part B
import airlineClasses
#import airlineExtras

def verifyDicts(cityCodeDict, aircraftCodeDict, flightDict):
    """
    A function to verify contents of 3 dictionaries
    """
    print 'verify dictionary creation by length'
    print 'length of cityCodeDict', len(cityCodeDict)
    print 'length of aircraftCodeDict', len(aircraftCodeDict)
    print 'length of flightDict', len(flightDict)
    print 'display a row from each dictionary to verify contents'
    for key in cityCodeDict.keys():
        print 'for key', key, 'the row is', cityCodeDict[key].cityCode, cityCodeDict[key].city
        break
    for key in aircraftCodeDict.keys():
        print 'for key', key, 'the row is', aircraftCodeDict[key].aircraftCode, aircraftCodeDict[key].name
        break 
    for key in flightDict.keys():
        print 'for key', key, 'the row is', flightDict[key].flightnum, flightDict[key].departCity,flightDict[key].arriveCity
        break
    
 
def getCityCodeDict():
    """
    A function to read in a CSV text file and create a dictionary with the
    key coming from the first field.  The dictionary value an Airport() object.
    
    The dictionary is returned.

    Each line of the CSV file contains 2 strings in double quotes.
    The double quotes and \n are removed from each line before insertion into the dictionary
    """
    
    filename = 'C:/Course/1905/Data/airports.csv'
    dictionary = {}
    for input in open(filename,'r'):
        if input:
            input = input.rstrip()               # remove the newline
            input = input.replace('"','')        # replace double quotes with null
            input = input.split(',')             # split at the comma      
            airport = airlineClasses.Airport(cityCode = input[0], city = input[1])    # create new object
            dictionary[airport.cityCode] = airport  # store in dictionary
    return dictionary

   
# Part C

def getAircraftCodeDict():
     
    filename = 'C:/Course/1905/Data/aircraft.csv'
    dictionary = {}
    for input in open(filename,'r'):
        if input:
            input = input.rstrip()               # remove the newline
            input = input.replace('"','')        # replace double quotes with null
            input = input.split(',')             # split at the comma      
            aircraft = airlineClasses.Aircraft(aircraftCode = int(input[0]), name= input[1])    # create new object
            dictionary[aircraft.aircraftCode] = aircraft  # store in dictionary
    return dictionary


def getFlightDict():
     
    filename = 'C:/Course/1905/Data/flights.csv'
    dictionary = {}
    for input in open(filename,'r'):
        if input:
            input = input.rstrip()               # remove the newline
            input = input.replace('"','')        # replace double quotes with null
            input = input.split(',')             # split at the comma      
            flight = airlineClasses.Flight( flightnum = int(input[1]),
                                            departCity = input[2],arriveCity = input[3],
                                            departTime = input[4], departDay = input[5],
                                            arriveTime = input[6], arriveDay = input[7],
                                            cost = float(input[8]),code = int(input[9])) 
            dictionary[flight.flightnum] = flight  # store in dictionary
    return dictionary


def writeDict(dictionary,filename):
  import pickle

  if not filename:
    print 'Must pass in a filename'
    return

  if not dictionary:
    print 'Must pass in a dictionary'
    return

  f = open(filename,'wb')
  pickle.dump(dictionary, f)
  

cityCodeDict = getCityCodeDict()
aircraftCodeDict = getAircraftCodeDict()
flightDict = getFlightDict()
verifyDicts(cityCodeDict, aircraftCodeDict, flightDict)

writeDict(cityCodeDict,'C:/Course/1905/Data/airports.pkl')
writeDict(aircraftCodeDict,'C:/Course/1905/Data/aircraft.pkl')
writeDict(flightDict,'C:/Course/1905/Data/flights.pkl')


