"""
Exercise 8.1 Accessing a MySQL database
"""
#Part A

import MySQLdb
import airlineClasses

def openConnection():
        
    host = 'localhost'
    name = 'user1'
    pw = 'ltree'
    db = 'airline'
    connection = MySQLdb.connect(host, name, pw, db)
    return connection


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
    A function to read in database table create a dictionary with the
    key coming from the first column.  The dictionary value an Airport() object.
    
    The dictionary is returned.

    Each row of the table contains 2 strings in double quotes.
    """
    table = 'airport'
    connection = openConnection()
    curs = connection.cursor()
    sqlcmd = "SELECT * FROM " + table
    d = {}
    
    curs.execute(sqlcmd)
    for row in curs.fetchall():
        airport = airlineClasses.Airport()
        airport.cityCode = row[0]
        airport.city = row[1]        
        d[airport.cityCode] = airport
        
    curs.close()
    connection.close()
    return d
    
# Part B


# For the first part of the exercise.
# Use these table names
# For Aircraft data the table = 'aircraft'
# For Flight data the table = 'flights'
# For Reservation data the table = 'reservations'
