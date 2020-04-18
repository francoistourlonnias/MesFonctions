"""
Exercise 7.1 Managing Files and Exceptions
Reading from pickle files
"""
# Part A

# For the second part of the exercise.
# Use these files to access the .pkl data
filename1 = 'C:/Course/1905/Data/airports.pkl'
filename2 = 'C:/Course/1905/Data/aircraft.pkl'
filename3 = 'C:/Course/1905/Data/flights.pkl'


# Part B

import airlineClasses
import pickle

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
    A function to read in a .pkl file create a dictionary with the
    key coming from the first field.  The dictionary value an Airport() object.
    
    The dictionary is returned.
    """

    dictionary = {}
    filename = 'C:/Course/1905/Data/airports.pkl'
    f = open(filename,'rb') 

    dictionary = pickle.load(f)
    f.close()
    return dictionary

# Part C
    