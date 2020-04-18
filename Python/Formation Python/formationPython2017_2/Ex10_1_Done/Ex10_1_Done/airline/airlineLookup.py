'''
airlineLoopup.py
'''

import sqlModule

cityCodeDict = sqlModule.getCityCodeDict()
reservationDict = sqlModule.getReservationDict()

def findCity(cityCode):
    if cityCodeDict.get(cityCode):
        d = {cityCode:cityCodeDict[cityCode].city}
    else:
        errorMsg = 'This airport is not served'
        d = {cityCode:errorMsg}
    return(d)


def findReservation(reservationId):

    if reservationDict.get(reservationId):
        d = {reservationId:reservationDict[reservationId].name}
    else:
        errorMsg = 'Invalid reservation number'
        d = {reservationId:errorMsg}
    return(d)