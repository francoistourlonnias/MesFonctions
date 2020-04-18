"""
Exercise 7.1 Managing Files and Exceptions.
Reading from CSV files
"""
# Part A

# For the first part of the exercise.
# Use these files to access the .csv data
filename1 = 'C:/\Users/ftourlon/Documents/5G_corner/FormationPython/aircraft.csv'
filename2 = 'C:/Users/ftourlon/Documents/5G_corner/FormationPython/aircraft.csv'
filename3 = 'C:/Users/ftourlon/Documents/5G_corner/FormationPython/flights.csv'



# Part B
import airlineClasses

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
    
    dictionary = {}
    for input in open(filename1,'r'):
        if input:
            input = input.rstrip()               # remove the newline
            input = input.replace('"','')        # replace double quotes with null
            input = input.split(',')             # split at the comma      
            airport = airlineClasses.Airport()   # create new object
            airport.cityCode = input[0]          # assign into new object
            airport.city = input[1]
            dictionary[airport.cityCode] = airport  # store in dictionary
    return dictionary

   

# Part C

def getAircraftCodeDict():
     
    dictionary = {}
    for input in open(filename2,'r'):
        if input:
            input = input.rstrip()               # remove the newline
            input = input.replace('"','')        # replace double quotes with null
            input = input.split(',')             # split at the comma      
            aircraft = airlineClasses.Aircraft()    # create new object
            aircraft.aircraftCode = int(input[0])          # assign into new object
            aircraft.name = input[1]
            dictionary[aircraft.aircraftCode] = aircraft  # store in dictionary
    return dictionary


def getFlightDict():
     
    dictionary = {}
#    for input in open(filename3,'r'):
    import csv 
    for input in csv.reader(open(filename1,'r')):
        if input:
#fait par reader            input = input.rstrip()               # remove the newline
#            input = input.replace('"','')        # replace double quotes with null
#            input = input.split(',')             # split at the comma      
            flight = airlineClasses.Flight(int(input[1]),input[2],input[3],input[4],
                                           input[5],input[6],input[7],float(input[8]),int(input[9])) 
            index = input[0]   # create new object
            dictionary[index] = flight  # store in dictionary
    return dictionary

cityCodeDict = getCityCodeDict()
aircraftCodeDict = getAircraftCodeDict()
flightDict = getFlightDict()
verifyDicts(cityCodeDict, aircraftCodeDict, flightDict)