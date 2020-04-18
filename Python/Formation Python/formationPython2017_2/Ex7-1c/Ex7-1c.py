"""
Exercise 7.1 Managing Files and Exceptions
Reading from shelve files
"""
# Part A

# For the third part of the exercise.
# Use these files to access the .dbm data
filename1 = 'C:/Course/1905/Data/airports.dbm'
filename2 = 'C:/Course/1905/Data/aircraft.dbm'
filename3 = 'C:/Course/1905/Data/flights.dbm'

# Part B


import airlineClasses
import shelve

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
    A function to read in a .dbm file create a dictionary with the
    key coming from the first field.  The dictionary value an Airport() object.
    
    The dictionary is returned.

    Each row of the table contains 2 strings in double quotes.
    """
    dictionary = {}
  
    f = shelve.open(filename1) 
    dictionary = f

    return dictionary


# Part C


