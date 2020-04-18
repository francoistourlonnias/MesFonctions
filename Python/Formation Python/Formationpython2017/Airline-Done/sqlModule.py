import MySQLdb
import airlineClasses


def openConnection():
            
    host = 'localhost'
    name = 'user1'
    pw = 'ltree'
    db = 'airline'
    connection = MySQLdb.connect(host, name, pw, db)
    return connection


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
    sqlcmd = "SELECT * FROM " + str(table)
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
    sqlcmd = "SELECT * FROM " + str(table)
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
    sqlcmd = "SELECT * FROM " + str(table)
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
    sqlcmd = "SELECT * FROM " + str(table)
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

