"""
Exercise 7.1 Managing Files and Exceptions.
Reading from CSV files
"""
# Part A

# For the first part of the exercise.
# Use these files to access the .csv data
filename1 = 'C:/Course/1905/Data/airports.csv'
filename2 = 'C:/Course/1905/Data/aircraft.csv'
filename3 = 'C:/Course/1905/Data/flights.csv'



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