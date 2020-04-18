
"""
    A module with the funtions to manage an airline.
"""

import sys
import airlineClasses

def listAll(dictionary):
    """
    A function to display a dictionary contents.

    A dictionary is the argument.
    """
    
    for v in dictionary.values():
        print v

def listAllCities(cityCodeDict): 
    """
    A function to display the cityCodeDict
    """
    
    print 'We travel to these cities'
    listAll(cityCodeDict)

def listAllAircraft(aircraftCodeDict):
    """
    A function to display the aircraftCodeDict.

    aircraftCodeDict is the argument.
    """  

    print 'We travel on these planes'
    listAll(aircraftCodeDict)

def listAllFlights(flightDict):
    """
    A function to display the flightDict

    flightDict is the argument.
    """  

    print 'We travel on these flights'
    listAll(flightDict)

def listFlightsTo(cityCode,flightDict): 
    """
    A function to display the flights per city.

    cityCode and flightDict are the arguments.
    """  
 
    for k in flightDict.keys():
        if cityCode == flightDict[k].arriveCity:
            print flightDict[k].flightnum, flightDict[k].departCity, flightDict[k].arriveCity

def lookupByCityName(city,cityCodeDict): 
    """
    A function to display if a city name is served.

    A city name and CityCodeDict are the arguments.
    """  

    for k in cityCodeDict.keys():
        if str(city) == cityCodeDict[k].city:
            print 'The code for', city, 'is', k    
            break
    else:
            print city, 'is not a city we fly to'
    
    
def lookupByCityCode(cityCode,cityCodeDict):
    """
    A function to display if a city code is served.

    A city code and CityCodeDict are the arguments.
    """  

    if cityCode in cityCodeDict.keys():
        print 'The code', cityCode, 'is for the city', cityCodeDict[cityCode].city
    else:
        print 'The code', cityCode, 'is not a city we serve'

def aircraftWithMostSeats(plist):
    """
    A function to display the plane with the most seats.

    A list of airline_classes.Aircraft objects are the arguments.
    """  

    most = current = airlineClasses.Workplane()
    for index in range(len(plist)):
        current = plist[index]
        if  most.maxSeats <  current.maxSeats:
            most.maxSeats = current.maxSeats
            most.aircraftCode = current.aircraftCode

    return most

def aircraftWithMostMiles(plist):
    """
    A function to display the plane that goes the most miles.

    A list of airline_classes.Passengerplan objects are the arguments.
    """
    
    most = current = airlineClasses.Workplane()
    most.maxMiles = 0
    for index in range(len(plist)):
        current = plist[index]
        if  most.maxMiles <  current.maxMiles:
            most.maxMiles = current.maxMiles
            most.aircraftCode = current.aircraftCode

    return most

def showFlightDetails(flightDict, flightnum):
    """
    A function to display details on a flight.

    The flightDict and flight number are the arguments.
    Results are written to standard output
    """
    flight = airlineClasses.Flight()
    for k in flightDict.keys():
        if flightDict[k].flightnum == flightnum:
            flight = flightDict[k]
            print 'Flight', flightnum, 'departs on',flight.departDay, flight.departTime, \
            'arrives on', flight.arriveDay, flight.arriveTime
            



def DailyRoundtrip(flightDict):
    """
    A function to find round trips in the flight schedule.

    The flightDict is the argument.
    Return a list of the round trips: flight number, city, and depart day
    """

    rtList = []
    for k in flightDict.keys():
        if flightDict[k].departCity == flightDict[k].arriveCity and \
           flightDict[k].departDay == flightDict[k].arriveDay:
               rt = str(flightDict[k].flightnum) + ' ' + flightDict[k].departCity + ' ' + \
               flightDict[k].departDay
               rtList.append(rt)

    return rtList
 
def planesPerCity(flightDict, aircraftCodeDict):
    """
    A function to list the planes for each city.

    The flightDict and aircraftCodeDict are the arguments.
    A dictionary is returned, its key is the  city code
    """

    d = {}

    for k in flightDict.keys():
        index = flightDict[k].departCity
        planeCode = flightDict[k].code
        if index not in d.keys():
            d[index] = [ planeCode ]
        elif planeCode not in d[index]:
            d[index].append(planeCode)

    return d
      

def citiesPerPlane(flightDict, aircraftCodeDict):
    """
    A function to list the cities for each plane.

    The flightDict and aircraftCodeDIct are the arguments.
    A dictionary is returned, its key is the aircraftCode.
    """

    d = {}

    for k in flightDict.keys():
        index = flightDict[k].code
        city = flightDict[k].departCity
        if index not in d.keys():
            d[index] = [ city ]
        elif city not in d[index]:
            d[index].append(city)
            
    return d

def flightsPerCity(flightDict, cityCode):
    """
    A function to list the flights for a city.

    The flightDict and cityCodeDIct are the arguments.
    A list of flight numbers is returned.
    """
    flights = []
    for k in flightDict.keys():
        if flightDict[k].departCity == cityCode:
            flights.append(flightDict[k].flightnum)

    return flights

def flightsPerCities(flightDict, departCityCode, arriveCityCode):
    """
    A function to list the flights for pair of cities.

    The flightDict and cityCodeDIct are the arguments.
    A list of flight numbers is returned.
    """
    flights = []
    for k in flightDict.keys():
        if flightDict[k].departCity == departCityCode and flightDict[k].arriveCity == arriveCityCode:
            flights.append(flightDict[k].flightnum)

    return flights

def isServed(cityCodeDict, cityCode):
    """
    A function to if a city is within the cityCodeDict.

    The cityCodeDIct cityCode are the arguments.
    A Boolean returned.
    """
    if cityCode in cityCodeDict.keys():
        return True
    else:
        return False

def convertCityToCode(city, cityCodeDict):
    """
    A function to if a city is within the cityCodeDict.

    The city and cityCodeDIct the arguments.
    A cityCode returned if found, else return None.
    """
    for k in cityCodeDict.keys():
        if city in cityCodeDict[k]:
            return k

    return(None)
    


    


