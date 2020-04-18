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


def verifyDicts(cityCodeDict, aircraftCodeDict, flightDict, reservationDict):
    """
    A function to verify contents of 3 dictionaries
    """
    print 'verify dictionary creation by length'
    print 'length of cityCodeDict', len(cityCodeDict)
    print 'length of aircraftCodeDict', len(aircraftCodeDict)
    print 'length of flightDict', len(flightDict)
    print 'length of reservationDict', len(reservationDict)
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
    for key in reservationDict.keys():
        print 'for key', key, 'the row is', reservationDict[key].reservationId, reservationDict[key].name
        break
# Part B

# For the first part of the exercise.
# Use these table names
# For Airport data the table = 'airport'
# For Aircraft data the table = 'aircraft'
# For Flight data the table = 'flights'
# For Reservation data the table = 'reservations'

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
    

def getAircraftCodeDict():
    """
    A function to read in a database and create a dictionary with the
    key coming from the first column.  The dictionary value an Aircraft() object.
    
    The dictionary is returned.
    
    Each row of the database table contains 1 integer and 1 string in double quotes.
    """
    table = 'aircraft'
    connection = openConnection()
    curs = connection.cursor()
    sqlcmd = "SELECT * FROM " + table
    d = {}
    
    curs.execute(sqlcmd)
    for row in curs.fetchall():
        aircraft = airlineClasses.Aircraft()
        aircraft.aircraftCode = row[0]
        aircraft.name = row[1]
        d[aircraft.aircraftCode] = aircraft
        
    curs.close()
    connection.close()
    return d


def getFlightDict():
    """
    A function to read in a database e and create a dictionary with the
    key coming from the first column.  The dictionary value is a Flight() object.
    
    The dictionary is returned.
    """
    table = 'flights'
    connection = openConnection()
    curs = connection.cursor()
    sqlcmd = "SELECT * FROM " + table
    d = {}
    
    curs.execute(sqlcmd)
    for row in curs.fetchall():
        flight = airlineClasses.Flight()
        flight.id = row[0]
        flight.flightnum = row[1]
        flight.departCity = row[2]
        flight.arriveCity = row[3]
        flight.departTime = row[4]
        flight.departDay = row[5]
        flight.arriveTime = row[6]
        flight.arriveDay = row[7]
        flight.cost = row[8]
        flight.code = row[9]
        d[flight.id] = flight
        
    curs.close()
    connection.close()
    return d

def getReservationDict():
    """
    A function to read in a database and create a dictionary with the
    key coming from the first column.  The dictionary value is a Reservation() object.
    
    The dictionary is returned.    
    """
    table = 'reservations'
    connection = openConnection()
    curs = connection.cursor()
    sqlcmd = "SELECT * FROM " + table
    d = {}
    
    curs.execute(sqlcmd)
    for row in curs.fetchall():
        flightData = airlineClasses.Flight(row[2],
                    row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        reservation = airlineClasses.Reservation(row[0],row[1],flightData)
        d[reservation.reservationId] = reservation

    curs.close()
    connection.close()
    
    return d

cityCodeDict = getCityCodeDict()
aircraftCodeDict = getAircraftCodeDict()
flightDict = getFlightDict()
reservationDict = getReservationDict()
verifyDicts(cityCodeDict, aircraftCodeDict, flightDict, reservationDict)
